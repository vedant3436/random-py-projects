from pytube import YouTube
while True:
    try:
        ytlink = input("Paste the link: ")
        yt_video = YouTube(ytlink)
        videos = yt_video.streams.all()
        vid = list(enumerate(videos))
        for i in vid:
            print(i)

        option = int(input("Enter the option: "))
        videos[option].download()
        print("Downloaded")
        break
    except:
        print("Did you paste a valid link? Try that again.")