# Ignore this - this is just needed for the program to run properly
import os
os.chdir(os.path.dirname(__file__))

# =========================

# Import OpenCV
import cv2

# Load an image
image = cv2.imread("../images/apple.jpeg")

# Convert this image into HSV


# Visualize the image with OpenCV
cv2.imshow("Image", image)

# Let's just look at the hue of the image
cv2.imshow("Hue", hsv[:, :, 0])

# And then wait for a key to be pressed to close the window
cv2.waitKey(0)