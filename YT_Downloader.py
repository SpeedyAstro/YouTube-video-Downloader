
# importing the module 
from pytube import YouTube

ch = {1 : "Title" ,2 : "Thumbnail", 3 : "Download Video" , 0 : "Exit" }


if __name__ == "__main__":
    # link of the video to be downloaded 
    # paste link 
    link = "https://www.youtube.com/watch?v=yMpt1AAIRPQ"
    yt = YouTube(link)
    while True:
        print(ch)
        oc = int(input())
        if oc == 1:
            # get_title
            print(yt.title)
        elif oc == 2:
            # get_thumbnail
            print(yt.thumbnail_url)
        elif oc == 3:
            # where to save 
            SAVE_PATH = "D:\python"
            # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
            # stream = yt.streams.first()
            
            try: 
            # downloading the video 
                # stream.download(SAVE_PATH)
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
            except: 
                print("Connection Error!") 
            print('Task Completed!')
        elif oc == 0:
            exit()
        else :
            print("Enter valid Choice")


