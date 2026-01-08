# DISCLAIMER

This project does not host, store, or distribute any copyrighted content.

Tune From List is an open-source software tool intended for personal, educational, research, and archival purposes only. It operates by accessing publicly available audio sources and processes all data locally on the user’s machine.

Users are solely responsible for ensuring that their use of this software complies with local copyright laws and the terms of service of any platforms they access.

The author of this project does not encourage, promote, or condone copyright infringement or unauthorized distribution of copyrighted material.

The author assumes no responsibility or liability for how this software is used, modified, redistributed, or integrated by third parties, including but not limited to individual users, organizations, automated systems, scripts, bots, artificial intelligence models, or other machine-based agents.

Any actions performed using this software are the sole responsibility of the end user or the system operating it. By using this software, you acknowledge and agree that all responsibility for its use lies entirely with you.

# Tune Fetcher

Tune Fetcher is a simple and minimalist desktop application that allows users to fetch publicly available audio content using a graphical user interface.

The project focuses on clarity, ease of use, and local processing. It does not host, distribute, or provide any media files and does not require user accounts or background services.


## Features

- Clean and minimal graphical user interface (GUI)
- Download audio by entering a track name
- Supports downloading single tracks
- Optional support for albums and playlists
- Audio conversion to MP3 format (320 kbps)
- Prevents file overwriting using unique identifiers
- Local processing only
- No advertisements
- No tracking
- No background services


## Interface Philosophy

Tune Fetcher is not a media player and not a streaming service.

It is designed as a lightweight utility focused solely on fetching audio in a clear, transparent, and user-controlled way. The interface intentionally avoids unnecessary complexity, settings overload, or visual noise.


## How It Works

1. The user enters a track name (or collection name) into the input field.
2. Publicly available audio sources are searched.
3. The selected content is fetched and processed locally.
4. Audio files are saved to a user-defined directory.

All operations are executed locally on the user’s machine.


## Requirements

- Python 3.8 or higher
- yt-dlp
- FFmpeg (must be available in system PATH)


## Installation

Clone the repository:
```
git clone https://github.com/your-username/tune-fetcher.git
cd tune-fetcher
```

Install dependencies:
```
python -m pip install yt-dlp
```

Verify FFmpeg installation:
```
ffmpeg -version
```

## Usage

Run the application:
```
python tune_fetcher.py
```
Use the graphical interface to:
- enter a track name
- start the download
- monitor progress


## Legal Disclaimer

This project does not host, store, or distribute any copyrighted content.

Tune From List is provided for educational use only. Users are solely responsible for ensuring that their use of this software complies with local copyright laws and the terms of service of any platforms they access.

The author of this project does not encourage, promote, or condone copyright infringement and assumes no responsibility for any misuse of this software by third parties.


## License

This project is licensed under the MIT License.
