from pytube import YouTube
from moviepy.editor import *
from google_images_download import google_images_download

def downloadYT(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")

def vidClip(vidPath, t1, t2, outPath, audio=True, createOutputFile=True):
    clip = VideoFileClip(vidPath)
    clip = clip.subclip(t1, t2)
    if not audio:
        clip = clip.set_audio(None)
    if createOutputFile:
        clip.write_videofile(outPath)
    return clip

def extractAudioClip(vidFile, t1, t2, outPath):
    audioClip = AudioFileClip(vidFile).subclip(t1, t2)
    audioClip.write_audiofile(outPath)

def cutByTimestamp(audioFile, timeStampFile):
    with open(timeStampFile) as file:
        timeInSeconds = []
        outPaths = []
        for line in file:
            timestamp = line.strip().split(":")
            outPaths.append(timestamp[1][3:] + ".mp3")
            timeInSeconds.append(int(timestamp[0])*60 + int(timestamp[1][:2]))
    fullAudioClip = AudioFileClip(audioFile)
    timeInSeconds.append(fullAudioClip.duration)
    print(timeInSeconds)
    print(outPaths)
    for i in range(len(outPaths)):
        clip = fullAudioClip.subclip(timeInSeconds[i]+0.9, timeInSeconds[i+1])
        clip.write_audiofile(outPaths[i])

#link = "https://www.youtube.com/watch?v=Z_BHv6RFVpY"
#downloadYT(link)
#clip("downloadedYTvids/test.mp4", 913, 916, "clippedVids/clip_test.mp4")
#cutByTimestamp("downloadedYTvids/cold_edit_songs.mp4", 'sampleTimestamps.txt')