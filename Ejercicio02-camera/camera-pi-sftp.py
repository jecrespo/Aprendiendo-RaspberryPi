#!/usr/bin/python3

# para instalar pysftp seguir los pasos:
#  sudo apt-get install python-dev
#  sudo apt-get install libffi-dev
#  sudo apt-get install libssl-dev
#  pip install pysftp (tarda bastante en instalar)

# Información sobre pysftp:
#  https://pypi.python.org/pypi/pysftp
#  documentación pysftp https://pysftp.readthedocs.io/en/release_0.2.9/
#  proyecto pysftp https://bitbucket.org/dundeemt/pysftp

import time
from picamera import PiCamera
import pysftp	
from datetime import datetime

sftp =  pysftp.Connection('hostname', username='me', password='secret')

camera = PiCamera()

camera.start_preview()
for i in range(360):	# 1 hora
    camera.capture('imagen.jpg')
    with sftp.cd('camera')
    	sftp.put('imagen.jpg')    # send the file
    print(datetime.now())
    time.sleep(10)	# 10 seconds
camera.stop_preview()
sftp.quit()
