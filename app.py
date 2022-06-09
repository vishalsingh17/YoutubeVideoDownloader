import streamlit as st
from yt_extractor import get_video

st.title("Download your favorite video HERE!!")

url = st.text_input("URL goes here", URL_goes_here)