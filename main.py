from pytube import YouTube
from pytube import Playlist

# Get Video
link = input("Enter the link: ")

# playlist or video?
if "list" in link:
    p = Playlist(link)
    print("Playlist found:")

    # if a video from a playlist if put in ask
    if "watch" in link:
        playlist_or_vid = input("Do you want to download the whole playlist or just this video? (y/n)")
        if playlist_or_vid == "y":

            # print out video names
            for url in p.video_urls[:3]:
                print(url)

            # download video names
            print('Downloading:', p.title)
            for audio in p.videos:
                print(audio.streams.get_by_itag("251").title)
                print("Downloading opus audio ...")
                audio.streams.get_by_itag("251").download()
        else:
            
            yt = YouTube(link)
            # Video Info
            print("Video found:")
            print("Title: ", yt.title)
            print("Number of views: ", yt.views)
            print("Length of video: ", yt.length, " seconds")
            print()

            # try to get opus audio
            try:
                # print(yt.streams.filter(only_audio=True))
                # print(yt.streams)
                ys = yt.streams.get_by_itag("251")
                ys.download()
                print("Downloading opus audio ...")
            except:
                print(yt.streams.filter(only_audio=True))
                stream = input("OPUS Audio not available, Select which audio stream you want (itag number):")
                ys = yt.streams.get_by_itag(stream)
                ys.download()
    else:

        # print out video names
        for url in p.video_urls[:3]:
            print(url)

        # download video names
        print('Downloading:', p.title)
        for audio in p.videos:
            print(audio.streams.get_by_itag("251").title)
            print("Downloading opus audio ...")
            audio.streams.get_by_itag("251").download()

else:
    yt = YouTube(link)
    # Video Info
    print("Video found:")
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length," seconds")
    print()

    # try to get opus audio
    try:
        #print(yt.streams.filter(only_audio=True))
        #print(yt.streams)
        ys = yt.streams.get_by_itag("251")
        ys.download()
        print("Downloading opus audio ...")
    except:
        print(yt.streams.filter(only_audio=True))
        stream = input("OPUS Audio not available, Select which audio stream you want (itag number):")
        ys = yt.streams.get_by_itag(stream)
        ys.download()
