import youtube_dl
from youtube_dl import DownloadError

def get_video(url):
    with ydl:
        try:
            video = ydl.extract(url, download=True)
        except DownloadError:
            return None

