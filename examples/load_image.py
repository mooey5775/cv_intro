# Ignore this - this is just needed for the program to run properly
import os
os.chdir(os.path.dirname(__file__))

# =========================

# Import OpenCV
import cv2

# Load an image
image = cv2.imread("../images/bikes.png")

# Let's see how this image is stored
print(image.shape)

# And then we can visualize the image with OpenCV
cv2.imshow("Image", image)

# And then wait for a key to be pressed to close the window
cv2.waitKey(0)