import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable


def download_video():
    try:
        url = link.get()
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_location = download_path.get()

        stream.download(output_path=download_location)
        status_label.config(text="Download Complete")
    except (RegexMatchError, VideoUnavailable) as e:
        status_label.config(text="Error: Invalid URL or Video Unavailable")


def browse_download_location():
    directory = filedialog.askdirectory()
    download_path.set(directory)


root = tk.Tk()
root.geometry('600x250')
root.title("YouTube Video Downloader")

# Labels
title_label = tk.Label(root, text="YouTube Video Downloader", font=('arial', 20, 'bold'))
title_label.pack()

link_label = tk.Label(root, text="Paste video link:", font=('arial', 15))
link_label.pack()

status_label = tk.Label(root, text="", font=('arial', 15))
status_label.pack()

# Entry
link = tk.StringVar()
link_entry = tk.Entry(root, width=60, textvariable=link)
link_entry.pack()

# Download Location
download_path = tk.StringVar()
download_path.set("")

browse_button = tk.Button(root, text="Browse", command=browse_download_location)
browse_button.pack()

download_path_label = tk.Label(root, text="Download Location:", font=('arial', 12))
download_path_label.pack()

download_path_entry = tk.Entry(root, width=60, textvariable=download_path)
download_path_entry.pack()

# Download Button
download_button = tk.Button(root, text="DOWNLOAD", font=('arial', 15, 'bold'), bg='pale violet red', padx=2,
                            command=download_video)
download_button.pack()

root.mainloop()
