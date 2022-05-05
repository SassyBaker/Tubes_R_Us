from downloader import download_video, get_video_data, convert_to_mp3


while True:  # Infinite loop closed by if statement
    url = input('Video URL ("q" to exit): ')
    if url.lower() == "q":
        exit()

    output = download_video(url)

    mp3_filename = convert_to_mp3(output)

    print(mp3_filename)
