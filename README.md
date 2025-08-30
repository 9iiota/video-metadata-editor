# MP4 Video Length Metadata Editor

A small Python script to edit the video length metadata field of an MP4 file.

## Usage
1. Download or clone the repository.
2. Drag and drop an mp4 file onto the script **or** run it from the command line:

```bash
python main.py path/to/video.mp4
```

3. Enter the desired video length (in milliseconds) when prompted.

## Notes
- This script modifies the file in place. Make a backup before using it.
- It only changes the metadata duration field, not the actual media length.
- Works on MP4 files.

## Requirements
- Python 3.6+
