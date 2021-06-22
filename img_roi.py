import cv2
import numpy
import imutils
#img read 
img=cv2.imread("rose.jpg")
#eye_ROI
eye = img[145:185, 155:200]
img[125:165, 25:70] = eye
#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey(0)
