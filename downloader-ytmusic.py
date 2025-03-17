import yt_dlp
import tkinter as tk
from tkinter import ttk, messagebox

def download_audio(urls, progress_var, download_button):
    total_urls = len([url for url in urls if url.strip()])
    completed = 0
    
    download_button.config(state=tk.DISABLED)  # Disable button while downloading
    
    for url in urls:
        if not url.strip():
            continue
        
        options = {
            'format': 'bestaudio/best',
            'outtmpl': f'%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [lambda d: update_progress(d, progress_var, total_urls, completed)]
        }
        
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        completed += 1
    
    messagebox.showinfo("Success", "All downloads complete!")
    progress_var.set(100)  # Set progress to 100% on completion
    download_button.config(state=tk.NORMAL)  # Enable button again

def update_progress(d, progress_var, total, completed):
    if d['status'] == 'downloading':
        percent = ((completed + d.get('downloaded_bytes', 0) / d.get('total_bytes', 1)) / total) * 100
        progress_var.set(percent)

# Setup UI
root = tk.Tk()
root.title("YouTube Music Downloader")
root.geometry("500x400")

tk.Label(root, text="Enter up to 10 YouTube URLs:").pack()
url_entries = []
for _ in range(10):
    entry = tk.Entry(root, width=50)
    entry.pack()
    url_entries.append(entry)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=400)
progress_bar.pack(pady=10)

download_button = tk.Button(root, text="Download", command=lambda: download_audio([e.get() for e in url_entries], progress_var, download_button))
download_button.pack(pady=10)

root.mainloop()
