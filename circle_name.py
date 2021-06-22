import cv2
import numpy
import imutils
#img read and display
img=cv2.imread("boy.jpg")
#REctangle over ROI
output = img.copy()
#cv2.rectangle(output, (170, 110), (270,220), (200, 150, 200), 3)
cir = circle_img = cv2.circle(img,(360,150), 100, (0,0,250), 2)
cv2.putText(cir, "Arun", (375,275),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,250), 2)
#cv2.imshow("Rectangle", output)
cv2.imshow ("circle", circle_img )
#line = cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow ("circle", cir ) 
cv2.waitKey(0) 
