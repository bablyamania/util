from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()
sleep(0.5)
camera.capture('/home/sahyog123/new1.jpg')
camera.stop_preview()