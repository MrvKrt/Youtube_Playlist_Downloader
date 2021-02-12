# install first pytube and moviepy if you have'nt before.
# pip install pytube
# pip install moviepy


from pytube import YouTube
from pytube import Playlist
import os 
import moviepy.editor as mp
import re

playlist = Playlist("playlist url")

for url in playlist:
    print(url)

for vid in playlist.videos:
    print(vid)

for url in playlist:
    YouTube(url).streams.first().download('/Users/username/Desktop/custom songs')

folder = "/Users/username/Desktop/custom songs"

#Coverting MP4 to MP3

for file in os.listdir(folder):
    if re.search('mp4', file):
        mp4_path = os.path.join(folder,file)
        mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)