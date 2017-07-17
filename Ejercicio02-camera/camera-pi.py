#!/usr/bin/python3
from picamera import PiCamera
from time import sleep
from ftplib import FTP

ftp = FTP('server','user','password')

camera = PiCamera()

camera.start_preview()
for i in range(500):
    camera.capture('imagen.jpg')
    file = open('imagen.jpg','rb')	 # file to send
    ftp.storbinary('STOR /html/imagen.jpg', file)  # send the file
    file.close()                                    # close file and FTP
camera.stop_preview()
ftp.quit()
