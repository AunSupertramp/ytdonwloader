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

# Download function with enhanced error handling
def download_video(url, path):
    if not url.strip():
        return "URL is empty. Please enter a valid YouTube video URL."
    try:
        yt = YouTube(url)
    except Exception as e:
        return f"Failed to fetch video data. Make sure the URL is correct. Error: {e}"

    try:
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
    except Exception as e:
        return f"Failed to find a suitable stream for download. Error: {e}"
    
    try:
        # Download the video to the default path
        stream.download(output_path=path)
        return f"Downloaded '{yt.title}' successfully to {path}"
    except Exception as e:
        return f"An error occurred during the download. Error: {e}"

# Button to download the video
if st.button('Download Video'):
    # Attempt to download the video to the default path
    message = download_video(url, default_download_path)
    if "successfully" in message:
        st.success(message)
    else:
        st.error(message)
