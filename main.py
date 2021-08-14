#  a python script to download the YouTube video

from pytube import YouTube
url = "https://www.youtube.com/watch?v=VPT_EIo89cc" #write the url link of your desired video link
video = YouTube(url) 
print(video.title)  # it will display the title of the YouTube video
video = video.streams.get_highest_resolution()
print(video.views)  # it will display views of the video
video.download()   # Here the last step!!! to download the video
