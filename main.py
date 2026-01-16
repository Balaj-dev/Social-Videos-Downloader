import yt_dlp
import os
import uuid

def download_link(url, download_folder='meow/'):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    unique_name = str(uuid.uuid4()) + '.%(ext)s'
    outtmpl = os.path.join(download_folder, unique_name)

    ydl_opts = {
        'format': 'best',   # <- simpler for FB/Instagram
        'outtmpl': outtmpl,
        'ignoreerrors': True,
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_link('https://www.instagram.com/reel/DTjXyCwkkbR/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ==')

