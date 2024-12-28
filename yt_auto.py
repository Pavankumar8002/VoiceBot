import webbrowser
import objc

def play_video(video_name):
    print(f"Playing video: {video_name}")
    url = f"https://www.youtube.com/results?search_query={video_name}"
    webbrowser.open(url)
