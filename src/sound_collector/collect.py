from pytubefix import YouTube

def collect_youtube(url:str, output_path:str):
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(output_path=output_path)


if __name__ == "__main__":
    import os

    url = "https://youtu.be/wSTbdqo-j74?si=ASugL4kftJRDb6dj"
    output_path = "/workspace/Storage/ssan/Data/raw/music/youtube/"
    os.makedirs(output_path, exist_ok = True)

    collect_youtube(url = url, output_path = output_path)