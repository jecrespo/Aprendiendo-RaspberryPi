#!/usr/bin/python3
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('video.h264')
sleep(20)
camera.stop_recording()
camera.stop_preview()
