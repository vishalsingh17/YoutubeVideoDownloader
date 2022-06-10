import streamlit as st
from pytube import YouTube

st.title("Download your favourite video HERE!!")
DOWNLOAD_PATH = './downloads/'
video_link = st.text_input("Enter the link of the video you want to download").split(',')
for i in video_link:
    YouTube(i).streams.first().download()
    yt = YouTube(i)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.download()
    # mp4files = yt.streams.filter('mp4')
    # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)

    # try:
    #     yt.download(DOWNLOAD_PATH)
    # except:
    #     st.write("There is some Error!")  
st.write('Videos Download Successfully!')
