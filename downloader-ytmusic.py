import yt_dlp
import colorama
from colorama import Fore

colorama.init(autoreset=True)

downloaded_links = set()

def download_audio(url):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

def repeat():
    while True:
        link = input("Enter YouTube link (or type 'exit' to exit): ").strip()
        
        if link.lower() == 'exit':
            print("exit the program.")
            break

        if link in downloaded_links:
            print(Fore.YELLOW + "⚠ This link has already been downloaded! ⚠")
        else:
            download_audio(link)
            downloaded_links.add(link)
            print("Download complete!\n")

repeat()
