import yt_dlp
import colorama
from colorama import Fore

colorama.init(autoreset=True)  # Inisialisasi colorama agar warna reset otomatis

downloaded_links = set()  # Menyimpan link yang sudah didownload

def download_audio(url):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Nama file sesuai judul video
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

def repeat():
    while True:
        link = input("Masukkan link YouTube (atau ketik 'exit' untuk keluar): ").strip()
        
        if link.lower() == 'exit':
            print("Keluar dari program.")
            break

        if link in downloaded_links:
            print(Fore.YELLOW + "⚠ Link ini sudah pernah didownload! ⚠")
        else:
            download_audio(link)
            downloaded_links.add(link)
            print("Download selesai!\n")

repeat()
