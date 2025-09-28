# Video Converter GUI

A simple **Linux GUI application** for converting videos using **FFmpeg**.  
Built with **Python** and **PyQt5**, it allows easy format conversion with support for odd-resolution videos.

---

## Features

- Drag-and-drop or file picker to select videos
- Convert videos to popular formats: MP4, AVI, MKV, MOV
- Automatic handling of videos with odd dimensions (width/height not divisible by 2)
- Progress bar to show conversion status
- Simple, lightweight GUI for Linux

---

## Requirements

- Python 3.x
- [FFmpeg](https://ffmpeg.org/) installed on your system
- Python packages:
  ```bash
  pip install pyqt5
