# mp4_to_mp3_converter
Simple converter to extract audio (mp3) from video files (mp4) using [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
ffmpeg has to be installed on the PC. It can be found [here](http://ffmpeg.org/).

For the installation of ffmpeg-python:
`pip install ffmpeg-python`

To use, change the PATH and DESTINATION variables in line 7 and 8.
Example:

```python
PATH = 'e:\\conv_test\\input\\'  # change to folder with video files you want to convert
DESTINATION = 'e:\\conv_test\\output\\'  # change to destination folder for mp3 files
```

Then simply run the file. It prints `completed`, after all files are converted.

It can process all kinds of filenames (even UTF-8 characters) and runs multi-threaded.
Your PC may become unresponsive during conversion, when converting lots of files. The converter will utilize close to 100% CPU.