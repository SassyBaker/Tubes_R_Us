import os
from downloader import download_video, get_video_data, convert_to_mp3
import streamlit as st

# Webpage elements
# st.title('Youtube Audio Downloader',)
st.markdown("<h1 style='text-align: center;'>Youtube Audio Downloader</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>You can download any public videos as mp3(128k)</h4>", unsafe_allow_html=True)
# st.write("You can download videos or mp3")
url = st.text_input(label="Video URL:", max_chars=256, key="vid_url")
submit = st.button("Steal It!")
