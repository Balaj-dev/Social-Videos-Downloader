from quopri import ESCAPE

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

while True:
    user= str(input("enter the Url of the file you want to downloade: "))
    if user == 'e':
        break
    else:
        pass
    download_link(user)


