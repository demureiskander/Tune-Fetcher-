import os
import re
import threading
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Listbox, filedialog
from tkinter import ttk
from yt_dlp import YoutubeDL

# Используем простой шрифт из Google Fonts
FONT = ("Roboto", 10)
APP_NAME = "EasyMusic Downloader"
OUTPUT_DIR = "Downloaded_Music"

# Функция для очистки имени файла
def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '', name)

# Функция для загрузки песни
def download_song(song_name: str, status_var: StringVar, queue_listbox, progress_bar):
    if not song_name.strip():
        messagebox.showwarning("Ошибка ввода", "Пожалуйста, введите название песни")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    safe_query = sanitize_filename(song_name)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s_%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'default_search': 'ytsearch1',
        'noplaylist': True,
        'quiet': True,
    }

    try:
        status_var.set("Загрузка...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([safe_query])
        
        progress_bar["value"] = 100
        status_var.set("Готово ✔")
        queue_listbox.insert('end', f"{song_name} - Скачано")
    except Exception as e:
        status_var.set("Ошибка")
        messagebox.showerror("Ошибка загрузки", str(e))

# Функция для обработки нажатия кнопки "Скачать"
def on_download_click(entry: Entry, status_var: StringVar, queue_listbox, progress_bar):
    song = entry.get()
    threading.Thread(
        target=download_song,
        args=(song, status_var, queue_listbox, progress_bar),
        daemon=True
    ).start()

# Функция для выбора папки
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        global OUTPUT_DIR
        OUTPUT_DIR = folder_selected

# Основная функция
def main():
    root = Tk()
    root.title(APP_NAME)
    root.geometry("500x400")
    root.resizable(False, False)

    # Заголовок
    Label(root, text=APP_NAME, font=("Roboto", 14, "bold")).pack(pady=15)

    # Поле для ввода названия песни
    Label(root, text="Введите название песни:", font=FONT).pack(pady=5)
    entry = Entry(root, width=45, font=FONT)
    entry.pack(pady=5)
    entry.focus()

    # Статус
    status_var = StringVar(value="Ожидание")
    
    # Кнопка "Скачать"
    download_button = Button(
        root,
        text="Скачать",
        width=20,
        command=lambda: on_download_click(entry, status_var, queue_listbox, progress_bar),
        font=FONT
    )
    download_button.pack(pady=15)

    # Прогресс-бар
    progress_bar = ttk.Progressbar(root, length=400, mode="determinate")
    progress_bar.pack(pady=5)

    # Очередь песен
    Label(root, text="Очередь песен:", font=FONT).pack(pady=5)
    queue_listbox = Listbox(root, width=50, height=6, font=FONT)
    queue_listbox.pack(pady=5)

    # Кнопка выбора папки
    folder_button = Button(
        root,
        text="Выбрать папку для сохранения",
        width=30,
        command=browse_folder,
        font=FONT
    )
    folder_button.pack(pady=10)

    # История скачиваний
    Label(root, text="История скачивания:", font=FONT).pack(pady=5)
    history_listbox = Listbox(root, width=50, height=4, font=FONT)
    history_listbox.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
