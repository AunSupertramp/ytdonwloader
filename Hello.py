import streamlit as st
from pytube import YouTube
import os

# Streamlit app title
st.title('YouTube Video Downloader')

# Input form for YouTube URL
url = st.text_input('Enter the YouTube video URL')

# Input for download path
path = st.text_input('Enter the download path (e.g., /home/user/downloads)')

# Download function
def download_video(url, path):
    try:
        yt = YouTube(url)
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        # Download the video
        stream.download(output_path=path)
        return f"Downloaded '{yt.title}' successfully."
    except Exception as e:
        return f"An error occurred: {e}"

# Button to download the video
if st.button('Download Video'):
    if not url or not path:
        st.error("Please enter both a video URL and a download path.")
    else:
        # Attempt to download the video
        message = download_video(url, path)
        st.success(message)
