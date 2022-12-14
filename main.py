from pytube import YouTube


# from pytube.exceptions import VideoUnavailable


def DownloadYoutubeAudio(link):
    """Downloads YouTube link to desktop in specified format"""
    yt = YouTube(link)
    yt = yt.streams.get_audio_only()
    try:
        yt.download()
        print("Mp3 download complete")
    except:
        print("Error downloading file")


if __name__ == "__main__":
    youtube_link = input("Copy and paste youtube link and press ENTER to download:\n")
    DownloadYoutubeAudio(youtube_link)
