from pytube import YouTube
from moviepy.editor import *

def downloadYT(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")

def clipNoAudio(vidPath, t1, t2, outPath, createOutputFile=True):
    clip = VideoFileClip(vidPath)
    clip = clip.subclip(t1, t2)
    if createOutputFile:
        clip.write_videofile(outPath)
    return clip

def clipWithAudio(vidPath, t1, t2, outPath, createOutputFile=True):
    clip = clipNoAudio(vidPath, t1, t2, outPath, createOutputFile=False)
    audioclip = AudioFileClip(vidPath).subclip(t1, t2)
    clip = clip.set_audio(audioclip)
    if createOutputFile:
        clip.write_videofile(outPath)
    return clip

clipWithAudio("test.mp4", 913, 916, "short_test.mp4")