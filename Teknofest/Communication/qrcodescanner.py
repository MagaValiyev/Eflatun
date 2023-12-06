import cv2
from pyzbar.pyzbar import decode
import time


def getcrcode():
    cam = cv2.VideoCapture(0)
    cam.set(5, 640)
    cam.set(6, 480)

    camera = True

    while camera:
        success, frame = cam.read()

        for i in decode(frame):
            # print(i.type)
            if(i):
                return i.data.decode('utf-8')
            
            print(i.data.decode('utf-8'))
            time.sleep(6)

            cv2.imshow('OurQRCodeScanner', frame)
            cv2.waitKey(3)

print(getcrcode())
