# File-Oraganization-Automations
# Automatic File Organizer

This Python script automatically organizes files in a specified folder by moving them to predefined directories based on their file extensions. It uses the `watchdog` library to monitor the folder for any file changes, such as newly downloaded files, and moves them to appropriate directories such as "Music," "Videos," "Images," "Documents," etc.

## Features

- Automatically moves files from the "Downloads" folder to the appropriate directories.
- Handles the following file types:
  - **Images** (e.g., `.jpg`, `.png`, `.gif`, etc.)
  - **Videos** (e.g., `.mp4`, `.avi`, `.mov`, etc.)
  - **Audio** (e.g., `.mp3`, `.wav`, `.aac`, etc.)
  - **Documents** (e.g., `.doc`, `.pdf`, `.xls`, etc.)
  - **Compressed Files** (e.g., `.zip`, `.rar`, `.7z`)
  - **Photoshop Files** (`.psd`, `.psb`)
  - **After Effects Files** (`.aep`)
- Handles file name conflicts by appending a counter to the file name if a file with the same name already exists in the destination folder.

## Prerequisites

- **Python 3.x** is required to run this script.
- Install the required Python dependencies:

```bash
pip install watchdog
