#importing the packages 
from pyimagesearch.transform import four_point_transform 
from skimage.filters import threshold_local
import numpy as np 
import argparse 
import cv2 
import imutils

# constructing the argument parser and parse the arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Path to the image to be scanned")
args = vars(ap.parse_args())

# Loading the image and compuite the ratio of the old height to the new height 
# Then we clone it and resizing 
image - cv2.imread(args["image"])
ratio = image.shape[0]/500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

#Now we conver the image to greyscale, blur it and find the ages in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
# show the original image and the edge detected image
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()