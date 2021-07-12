import logging
import requests
import os
import time
import datetime
import socket


def get_url_list():
    urls = dict()
    urls['its']='https://www.its.ac.id/wp-content/uploads/2020/07/Lambang-ITS-2-300x300.png'
    urls['sch']='https://www.its.ac.id/news/wp-content/uploads/sites/2/2019/10/home-bar.e1ac3112.png'
    urls['fb']='https://www.facebook.com/images/fb_icon_325x325.png'
    urls['twt']='https://cdn.cms-twdigitalassets.com/content/dam/help-twitter/twitter_logo_blue.png.twimg.768.png'
    urls['ig']='https://www.instagram.com/static/images/ico/favicon-200.png/ab6eff595bb1.png'
    return urls


def download_broadcast_gambar(url=None,tuliskefile=False, target_ip=None, target_port=None):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    time.sleep(2) #untuk simulasi, diberi tambahan delay 2 detik

    # download
    namafile = os.path.basename(url)
    if (tuliskefile):
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()

    # broadcast gambar
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f"broadcast file {namafile}")
    image_file = open(f"{namafile}","rb")
    image_bytes = image_file.read()
    sock.sendto(image_bytes, (target_ip, target_port))

    # waktu
    waktu_process = datetime.datetime.now() - waktu_awal
    waktu_akhir =datetime.datetime.now()
    logging.warning(f"download dan broadcast {namafile} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
    return waktu_process
