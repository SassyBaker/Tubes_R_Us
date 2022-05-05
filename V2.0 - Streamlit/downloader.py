import os
from pytube import YouTube


# Get info
def get_video_data(video_url):
    video = YouTube(video_url)

    return {
        'title': video.title,
        'thumbnail': video.thumbnail_url,
        'length': video.length,
        'total_views': video.views,
        'published_date': video.publish_date,
        'streams': video.streams,
    }


# Split Absolut Directory
def split_dir(abs_dir):
    base, ext = os.path.splitext(abs_dir)
    filename = os.path.basename(base)
    return {
        'full_path': abs_dir,
        'base_dir': base,
        'extension': ext,
        'filename': filename
    }


# Downloader
def download_video(video_url, audio=True):
    return split_dir(YouTube(video_url).streams.filter(only_audio=audio).first().download(output_path='temp'))


# Convert to MP3
def convert_to_mp3(file):
    mp4_file = file['full_path']
    mp3_file = file['base_dir'] + '.mp3'

    cmd = f"ffmpeg -i '{mp4_file}' '{mp3_file}'"
    os.system(cmd)

    return mp3_file
