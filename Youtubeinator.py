#Youtube Download Tool by Benjamin Jack Cullen
import pafy
def choice(x, url, video, streams):
    if x=="1":
        print("finding available video formats...")
        for s in streams:
            print("Resolution:",s.resolution)
            print("Extension:",s.extension)
            print("File-Size:",s.get_filesize())
            print("URL:",s.url,"\n")
        print("comparing resolution...")
        best = video.getbest()
        print("Best resolution:",best.resolution, best.extension)
        print("Getting URL...")
        print(best.url)
        print("downloading Video:", video.title)
        best.download(quiet=False)
        input('\nCompleted... Press any key to exit.')
        exit()
    elif x=="2":
        print("finding available audio formats...")
        audiostreams = video.audiostreams
        for a in audiostreams:
            print("Bitrate:",a.bitrate)
            print("Extension:",a.extension)
            print("File-Size:",a.get_filesize(),"\n")
        print('comparing bitrate...')
        bestaudio = video.getbestaudio()
        print("Best audio:", bestaudio.bitrate)
        print("Downloading Audio:", video.title)
        bestaudio.download()
        input('\nCompleted... Press any key to exit.')
        exit()
    else:
        menu()
def menu(url, video, streams):
    print("\nTitle      :",video.title)
    print("Author     :",video.author)
    print("Rating     :",video.rating)
    print("Views      :",video.viewcount)
    print("Description:",video.description)
    print("\nOptions:")
    print("1. Download Video.")
    print("2. Download Audio.")
    x=input("Select :")
    choice(x, url, video, streams)
print('\nWELCOME TO YOUTUBINATOR!\n')
url = input("Enter URL :")
video = pafy.new(url)
streams = video.streams
print('url appears acceptable...')
menu(url, video, streams)
