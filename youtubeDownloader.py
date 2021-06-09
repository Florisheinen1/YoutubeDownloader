import sys

FILE_TYPES = ["mp3", "wav", "mp4"]
USAGE = "Usage: ytdownload " + str(FILE_TYPES) + " <url>"

if len(sys.argv) != 3:
	print("Error: Invalid arguments")
	print(USAGE)
	exit()

extension = sys.argv[1]
if not extension in FILE_TYPES:
	print("Error: Unsupported file extension '" + extension + "'. Only " + str(FILE_TYPES) + " is allowed")
	exit()


link = sys.argv[2]

from pytube import YouTube
try:
	stream = YouTube(link).streams.get_highest_resolution()
except Exception as e:
	print("Error: Could not find streams of link: '" + str(link) + "'")
	exit()

print("Downloading video...")
video = stream.download()


import shutil
if extension == "mp4":
	shutil.move(str(video), r"C:\Users\Flori\Downloads")
	print("Done.")
	exit()
else:
	print("Extracting audio from video...")
	
	from moviepy.editor import *
	filePath = video.split(".mp4", 1)[0] + "." + extension

	video_clip = VideoFileClip(video)
	audio_clip = video_clip.audio
	audio_clip.write_audiofile(filePath)

	audio_clip.close()
	video_clip.close()

	import os
	os.remove(video)
	shutil.move(filePath, r"C:\Users\Flori\Downloads")