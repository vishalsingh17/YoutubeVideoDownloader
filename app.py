import streamlit as st
from pytube import YouTube

URLS = st.text_input('URL').split(',')
for URL in URLS:
    yt = YouTube(URL)
    st.write(yt.title)
    stream_values = yt.streams.filter(file_extension='mp4')
    st.write(stream_values[0:3])
    stream = yt.streams.get_by_itag(133)
    stream.download()