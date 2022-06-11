import streamlit as st
from pytube import YouTube

URLS = st.text_input('URL').split(',')
for URL in URLS:
    yt = YouTube(URL)
    st.write(yt.title)
    st.write(yt.streams.filter(file_extension='mp4'))
    stream = yt.streams.get_by_itag(399)
    stream.download()