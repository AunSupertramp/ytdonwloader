import streamlit as st
from pytube import YouTube
import os

# Streamlit app title
st.title('YouTube Video Downloader')

# Input form for YouTube URL
url = st.text_input('Enter the YouTube video URL')

# Default download path (change this to your preferred path)
default_download_path = './downloads'

# Ensure the default download path exists
if not os.path.exists(default_download_path):
    os.makedirs(default_download_path)

# Download function
def download_video(url, path):
    try:
        yt = YouTube(url)
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        # Download the video to the default path
        stream.download(output_path=path)
        return f"Downloaded '{yt.title}' successfully to {path}"
    except Exception as e:
        return f"An error occurred: {e}"

# Button to download the video
if st.button('Download Video'):
    if not url:
        st.error("Please enter a video URL.")
    else:
        # Attempt to download the video to the default path
        message = download_video(url, default_download_path)
        st.success(message)
