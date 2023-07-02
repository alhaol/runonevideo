import streamlit as st

# Define a selectbox and options for the user to choose the video
video_option = st.selectbox(
    'What video to run?',
    ('HateRunning', 'Do5Min')
)

# Depending on the option chosen by the user, the video file path changes
if video_option == 'HateRunning':
    video_file = 'videos/haterunning.mp4'
elif video_option == 'Do5Min':
    video_file = 'videos/do5min.mp4'


# Display the video
video_file = open(video_file, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
