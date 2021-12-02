# Python 3.9
import glob
import os

import ffmpeg

# using this path format: 'c:\\users\\admin\\videos\\' ending with \\
PATH = ''  # change to folder with video files you want to convert
DESTINATION = ''  # change to destination folder for mp3 files


def convert(video: str, destination_path: str):
    destination_path = destination_path + os.path.splitext(os.path.basename(video))[0] + '.mp3'
    conv_process = (
        ffmpeg
            .input(video)  # read
            .output(destination_path, format='mp3', acodec='libmp3lame', ac=2, ar='44100',
                    audio_bitrate=192000)  # write and config
            .overwrite_output()  # always overwrite
            .run_async(quiet=False)  # run conversion async
    )
    return conv_process


def main():
    path = PATH  # path to read files from
    destination = DESTINATION  # destination for converted files
    # read all mp4 files in dir and recursive folders
    files = list(glob.glob(path + "**/*.mp4", recursive=True))
    return_processes = []
    for file in files:  # loop through all files
        return_processes.append(convert(file, destination))  # convert file
    for process in return_processes:
        process.communicate()
    print('completed')


if __name__ == "__main__":
    main()
