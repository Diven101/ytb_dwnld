from tkinter import *
from pytube import Youtube
from tkinter import messagebox,filedialog


def browse():
    download_directory = filedialog.askdirectory(initialdir= "/Users/diven/Downloads")
    down_path.set(download_directory)
def download():
    youtube_link = video_link.get()
    download_folder = down_path.get()
    get_video = YouTube(youtube_link)
    videostream = get_video.streams.first()
    videostream.download(download_folder)

    messagebox.showinfo("success","video in downloads")

link_label = Label(root,text = "Youtube Link: ",bg="red")
link_label.grid(row=1,column=0,padx=10,pady=10)

link_text = Entry(root,width=50,textvariable = video_link)
link_text.grid(row=1,column=1,padx=10,pady=10)

browse_label = Label(root,text="Browse folder",bg="red")
browse_label.grid(row=2,column=0,padx=10,pady=10)

browse_text = Entry(root,width=50,textvariable = down_path)
browse_text.grid(row=2,column=1,padx=10,pady=10)

browse_b = Button(root,text="Browse",bg='blue',width=5,command = browse)
browse_b.grid(row=3,column=0)

download_b = Button(root,text="download",bg='blue',width=10,command=download)
download_b.grid(row=3,column=1)



root = Tk()
root.config(bg="black")
root.title("Youtube downloader: ")
root.geometry("600x180")


