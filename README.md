# YouTube Downloader

A Python-based YouTube downloader built with **yt-dlp**.

This project is being developed as a practical Python project to learn how to work with external libraries, URLs, video metadata, file downloads, error handling, and clean project structure.

> **Note:** Use this project only to download content that you own, have permission to download, or that is legitimately available for download. Please respect YouTube's Terms of Service and copyright laws.

---

## Features

The project is being developed step by step.

### Current Features

* Download videos from YouTube
* Use `yt-dlp` for video extraction and downloading
* Specify a YouTube URL
* Select download formats
* Extract video information
* Basic error handling

### Planned Features

* [ ] URL validation
* [ ] Video metadata display
* [ ] Audio-only downloads
* [ ] Video quality selection
* [ ] Format selection
* [ ] Custom download directory
* [ ] Progress bar
* [ ] Download progress hooks
* [ ] Better error handling
* [ ] Command-line interface
* [ ] Simple graphical user interface
* [ ] Clean project architecture
* [ ] Configuration system
* [ ] Logging
* [ ] Unit tests

---

## Technologies

This project uses:

* **Python**
* **yt-dlp**
* **Git**
* **GitHub**

---

## Project Structure

The project will gradually evolve into a cleaner structure.

```text
Youtube-Downloader/
│
├── src/
│   ├── main.py
│   ├── downloader.py
│   ├── extractor.py
│   ├── validator.py
│   └── utils.py
│
├── downloads/
│   ├── video/
│   └── audio/
│
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
```

The structure may change as the project becomes more advanced.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/iamhoss14/Youtube-Downloader.git
```

Move into the project directory:

```bash
cd Youtube-Downloader
```

---

### 2. Create a virtual environment

Using a virtual environment keeps project dependencies isolated. Humanity invented environments specifically so one Python project doesn't destroy another one.

Create an environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

Install `yt-dlp`:

```bash
pip install yt-dlp
```

Or install all project dependencies:

```bash
pip install -r requirements.txt
```

---

## Basic Usage

Run the downloader:

```bash
python src/main.py
```

Enter a YouTube URL when requested.

Example:

```text
Enter YouTube URL:
https://www.youtube.com/watch?v=VIDEO_ID
```

The downloader will process the URL and download the selected content.

---

## Using yt-dlp

The main library used by this project is `yt-dlp`.

A basic example:

```python
import yt_dlp

url = "https://www.youtube.com/watch?v=VIDEO_ID"

options = {
    "format": "best"
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])
```

The `YoutubeDL` class is the main interface used to configure and perform downloads.

---

## Extracting Video Information

`yt-dlp` can also extract information without downloading the video.

```python
import yt_dlp

url = "https://www.youtube.com/watch?v=VIDEO_ID"

with yt_dlp.YoutubeDL() as ydl:
    info = ydl.extract_info(url, download=False)

print("Title:", info["title"])
print("Uploader:", info["uploader"])
print("Duration:", info["duration"])
print("URL:", info["webpage_url"])
```

Using:

```python
download=False
```

means that `yt-dlp` extracts the information but does not download the video.

This is useful for displaying information to the user before starting a download.

---

## Selecting a Format

`yt-dlp` supports different video and audio formats.

For example:

```python
options = {
    "format": "best"
}
```

Then:

```python
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])
```

More advanced format selection will be added as the project develops.

---

## Audio Download

One of the planned features is downloading audio separately.

A possible configuration is:

```python
options = {
    "format": "bestaudio"
}
```

Additional post-processing can be added later using `FFmpeg`.

---

## Download Directory

The project will support organized download directories.

Example:

```text
downloads/
│
├── video/
│   └── example_video.mp4
│
└── audio/
    └── example_audio.mp3
```

This keeps downloaded files separate from the source code.

---

## Error Handling

The downloader should handle common errors such as:

* Invalid YouTube URLs
* Unsupported URLs
* Network connection problems
* Video unavailable
* Private videos
* Age-restricted content
* Missing dependencies
* Invalid format selections
* Download failures

Example:

```python
import yt_dlp

try:
    with yt_dlp.YoutubeDL({"format": "best"}) as ydl:
        ydl.download([url])

except yt_dlp.utils.DownloadError as error:
    print("Download failed:", error)
```

The error-handling system will become more robust as the project develops.

---

## Requirements

The main dependency is:

```text
yt-dlp
```

You can install it with:

```bash
pip install yt-dlp
```

If FFmpeg is required for audio conversion or merging formats, it should also be installed on the system.

---

## Learning Goals

This project is not only about downloading YouTube videos.

The main goal is to practice real-world Python development.

Through this project, I am learning:

* Python project structure
* Working with external libraries
* Reading documentation
* API/library usage
* Object-oriented programming
* Exception handling
* File handling
* URL validation
* Working with metadata
* Command-line applications
* Dependency management
* Git and GitHub
* Writing clean and maintainable code
* Debugging real-world problems

---

## Development Roadmap

### Phase 1: Learn yt-dlp

* [x] Install `yt-dlp`
* [x] Understand `YoutubeDL`
* [x] Understand `extract_info()`
* [x] Understand `download=False`
* [x] Download a basic video
* [ ] Understand format selection
* [ ] Understand metadata
* [ ] Understand progress hooks

### Phase 2: Basic Downloader

* [ ] Accept a URL from the user
* [ ] Validate the URL
* [ ] Extract video information
* [ ] Display title and duration
* [ ] Download the video
* [ ] Handle errors

### Phase 3: Better Downloader

* [ ] Quality selection
* [ ] Audio-only mode
* [ ] Custom output directory
* [ ] Progress display
* [ ] Better error messages

### Phase 4: Project Architecture

* [ ] Separate downloader logic
* [ ] Create URL validator
* [ ] Create format manager
* [ ] Create utility functions
* [ ] Add configuration
* [ ] Add logging

### Phase 5: Testing

* [ ] Add unit tests
* [ ] Test URL validation
* [ ] Test error handling
* [ ] Test downloader logic

### Phase 6: User Interface

* [ ] Build CLI interface
* [ ] Add interactive menus
* [ ] Add GUI
* [ ] Improve user experience

---

## Example Workflow

The final application should follow a workflow similar to:

```text
User
 │
 ▼
Enter YouTube URL
 │
 ▼
Validate URL
 │
 ▼
Extract Video Information
 │
 ▼
Show Video Details
 │
 ▼
Choose Download Type
 │
 ├── Video
 │
 └── Audio
 │
 ▼
Choose Quality / Format
 │
 ▼
Start Download
 │
 ▼
Show Progress
 │
 ▼
Save File
```

---

## Future Improvements

Possible future improvements include:

* Playlist downloading
* Channel downloading
* Multiple format options
* Download queue
* Concurrent downloads
* Resume interrupted downloads
* Configuration files
* Download history
* Better terminal interface
* GUI application
* Web interface
* Docker support
* Automated testing
* CI/CD with GitHub Actions

Some of these features may be added only after the core downloader is stable.

---

## Why I Built This Project

I created this project to improve my Python programming skills by building something practical instead of only completing small exercises.

The project gives me an opportunity to work with a real-world Python library and gradually transform a simple script into a structured application.

The development process follows this approach:

```text
Learn
  ↓
Build a small feature
  ↓
Test it
  ↓
Understand the code
  ↓
Refactor
  ↓
Commit to Git
  ↓
Build the next feature
```

---

## Git Workflow

Changes are committed regularly during development.

Example:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Add basic video downloader"
```

Push:

```bash
git push
```

Example commit history:

```text
Add yt-dlp dependency
Add basic video downloader
Add video metadata extraction
Add URL validation
Add format selection
Add audio download support
Improve error handling
Add download progress
Refactor downloader architecture
Add tests
```

---

## Project Status

**Status:** 🚧 In Development

This project is being developed incrementally while learning `yt-dlp`, Python project architecture, and real-world software development practices.

---

## Disclaimer

This software is provided for educational and personal development purposes.

Users are responsible for ensuring that their use of the software complies with applicable laws, copyright restrictions, and the terms of the platforms they access.

Do not use this project to download content that you do not have the legal right or permission to download.

---

## Author

**Amirhossein**

GitHub:

https://github.com/iamhoss14

---

## License

This project is intended as an educational project.

A formal open-source license may be added as the project develops.
