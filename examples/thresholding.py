# Ignore this - this is just needed for the program to run properly
import os
os.chdir(os.path.dirname(__file__))

# =========================

# MIN AND MAX HUES
min_hue = 150
max_hue = 180

# Import OpenCV
import cv2

# Load an image
image = cv2.imread("../images/apple.jpeg")

# Convert this image into HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Visualize the image with OpenCV
cv2.imshow("Image", image)

# Let's threshold the image
# First, we need to make our min and max thresholds
min_thresh = (min_hue, 0, 0)
max_thresh = (max_hue, 255, 255)

# Now, OpenCV has a nice function to threshold an image
mask = cv2.inRange(hsv, min_thresh, max_thresh)

# Look at our new image
cv2.imshow("Thresh", mask)

# And then wait for a key to be pressed to close the window
cv2.waitKey(0)