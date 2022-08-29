#Download all videos in a YouTube playlist as mp3s. Make sure the playlist has public access!

from pytube import Playlist
import youtube_dl

playlistLink = input("YouTube Playlist Link: ")
playlist = Playlist(playlistLink)

print("Total video to download: ", len(playlist.video_urls))

for url in playlist.video_urls:
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = url,download=False
    )
    
    filename = f"{video_info['title']}.mp3"
    
    options={
        'format':'worstaudio/worst',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
