#!/usr/bin/python3
import time
from picamera import PiCamera
from time import sleep
from ftplib import FTP
from datetime import datetime

ftp = FTP('server','user','password')

camera = PiCamera()

camera.start_preview()
for i in range(360):	# 1 hora
    camera.capture('imagen.jpg')
    file = open('imagen.jpg','rb')	# file to send
    ftp.storbinary('STOR /html/servicios/imagen.jpg', file)	# send the file
    file.close()	# close file and FTP
    print(datetime.now())
    time.sleep(10)	# 10 seconds
camera.stop_preview()
ftp.quit()
