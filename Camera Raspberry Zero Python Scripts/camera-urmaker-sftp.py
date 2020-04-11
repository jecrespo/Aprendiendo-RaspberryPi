#!/usr/bin/python3
import time
from picamera import PiCamera
from time import sleep
import pysftp	# pip install pysftp https://pypi.python.org/pypi/pysftp
from datetime import datetime

# documentación pysftp https://pysftp.readthedocs.io/en/release_0.2.9/
# proyecto pysftp https://bitbucket.org/dundeemt/pysftp

sftp =  pysftp.Connection('hostname', username='me', password='secret')

camera = PiCamera()

camera.start_preview()
for i in range(360):	# 1 hora
    camera.capture('imagen.jpg')
    with sftp.cd('camera')
    	sftp.put('./imagen.jpg')    # send the file
    print(datetime.now())
    time.sleep(10)	# 10 seconds
camera.stop_preview()
sftp.quit()
