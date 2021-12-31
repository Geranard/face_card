import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

def resolution(width, height):
    camera.set(3, width) # width
    camera.set(4, height) # height

def rescale(frame, scale):
    scale = 10
    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 100)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

resolution(1920, 1080)

filename = "video.avi"

while True:
    check, frame = camera.read() # capture frame by frame from camera

    cv.imshow("original", frame) # display original frame

    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # changing it to gray
    # cv.imshow("gray", gray)

    # rescaled_frame = rescale(frame, 50) # rescale the frame
    # cv.imshow("rescaled", rescaled_frame)

    

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv.destroyAllWindows()
