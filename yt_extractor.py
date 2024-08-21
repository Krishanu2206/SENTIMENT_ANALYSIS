import yt_dlp as youtube_dl

ydl = youtube_dl.YoutubeDL()

##DOWNLOAD A VIDEO FILE AND EXTRACT THE INFOS
def get_video_infos(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download=False
        )
        if "entries" in result:
            return result["entries"][0] 
        return result
    
def get_audio_url(video_info):
    for f in video_info["formats"]:
        if f["ext"] == "m4a":
            return f["url"]

if __name__ == "__main__":
    video_info=get_video_infos("https://www.youtube.com/watch?v=rz_rus8Vg6Q")
    audio_url = get_audio_url(video_info)
    print(f"Audio URL: {audio_url}")