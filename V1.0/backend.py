from pytube import YouTube
"""Regex fix: https://stackoverflow.com/a/71903013"""


# Initialize Video Object
def video_object(url):
    return YouTube(url)


# Get Video Info
def video_meta_data(video):
    return {
        'title': video.title,
        'thumbnail': video.thumbnail_url,
        'length': video.length,
        'streams': video.streams
    }


# Download Video
def download_video(video, options):
    pass


# Convert File
def convert_to_audio(filename):
    pass
