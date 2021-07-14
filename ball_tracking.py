# Ignore this - this is just needed for the program to run properly
import os
os.chdir(os.path.dirname(__file__))

# =========================

from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time

LOWER_THRESH = (29, 86, 6)
UPPER_THRESH = (64, 255, 255)

vs = cv2.VideoCapture("videos/ball.mp4")

# wait for video to be opened
time.sleep(2.0)

while True:
    image = vs.read()[1]

    # close if video is over
    if image is None:
        break

    image = imutils.resize(image, width=600)

    # WRITE CODE HERE
    
    
    # IGNORE THIS PART - JUST SOME CONTOUR PROCESSING
    # ==============================================
    # cnts = imutils.grab_contours(cnts)

    # if len(cnts) > 0:
    #     c = max(cnts, key=cv2.contourArea)
    #     ((x, y), radius) = cv2.minEnclosingCircle(c)
    #     M = cv2.moments(c)
    #     center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    #     if radius > 10:
    #         cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
    #         cv2.circle(image, center, 5, (0, 0, 255), -1)
    # ========================================================

    # Show the final image

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
