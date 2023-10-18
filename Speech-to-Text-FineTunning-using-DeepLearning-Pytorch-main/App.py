import streamlit as st
import pandas as pd
import numpy as np
from pytube import YouTube
from transformers import pipeline

# My main Functions
def video_to_audio(video_url = 'None'):
    if video_url == 'None':
        return
    try:
        video = YouTube(video_url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"{video.title}.wav")
        st.info("The video is downloaded in form of Audio")
        return video_url
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")
        return video_url

def audio_to_text(path):
    pass

if __name__ == '__main__':
    st.title('Extract Text from Video and Summerize it')
    st.subheader('Place Youtube Video Link')
    video_url = st.text_input('Youtube video Url', placeholder='Enter URL Here')
    video_url = str(video_url)
    url = ''

    if st.button('Submit the Url' ):
        url = video_to_audio(video_url)  # Function Call

          
    
    st.subheader('Extracted Text from Video')
    path = 'Best Short Motivational Speech Video - 24 HOURS - 1-Minute Motivation #2.wav'
    video_Text = st.text_area("Text of Video", url)

    st.subheader('Text Sumerization')
    sum_text = st.text_area("Sumerization of Text", '')    





#st.subheader('Youtube video Url')







