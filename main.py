# Video Processing Functions

from pytube import YouTube
from moviepy.editor import *

def downloadYT(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")

def clip(vidPath, t1, t2, outPath, audio=True, createOutputFile=True):
    clip = VideoFileClip(vidPath)
    clip = clip.subclip(t1, t2)
    if not audio:
        clip = clip.set_audio(None)
    if createOutputFile:
        clip.write_videofile(outPath)
    return clip

#downloadYT("https://www.youtube.com/watch?v=z6X7demVALo&t=917s")
#clip("test.mp4", 913, 916, "clip_test.mp4", audio=False)