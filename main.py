from pytube import YouTube

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()  
        print(f"{yt.title} has been downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Please enter the video URL: ")  # URL'yi kullanıcıdan alıyoruz
    download_video(url)
