import streamlit as st
from pytube import YouTube, Playlist

option = st.sidebar.radio("Select one:", ['Download using URL', 'Download playlist'])
if option == 'Download using URL':
    URLS = st.text_input('Enter the video URL').split(',')
    for URL in URLS:
        yt = YouTube(URL)
        st.write(yt.title)
        st.write(yt.streams.filter(file_extension='mp4'))
        st.write(yt.streams.filter(only_audio=True))
        stream_video = yt.streams.get_by_itag(137)
        stream_audio = yt.streams.get_by_itag(251)
        stream_video.download()
        stream_audio.download()
elif option == 'Download playlist':
    Playlist_URL = st.text_input('Enter the playlist URL')
    p = Playlist(Playlist_URL)
    for url in p.video_urls:
        try:
            yt = YouTube(url)
        except VideoUnavaible:
            print(f'Video {url} is unavaialable, skipping.')
        else:
            print(f'Downloading video: {url}')
            yt.streams.first().download()