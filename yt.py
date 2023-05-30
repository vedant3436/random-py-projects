# pip install pytube before executing
from pytube import YouTube
while True:
    try:
        ytlink = input("Paste the link: ")
        yt_video = YouTube(ytlink)
        videos = yt_video.streams.all() #list of all available types/resolutions for download
        vid = list(enumerate(videos)) #easier for user to pick from the options
        for i in vid:
            print(i)

        option = int(input("Enter the option: "))
        videos[option].download()
        print("Downloaded")
        break
    except:
        print("Did you paste a valid link? Try that again.")
