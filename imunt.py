#-*- coding: utf-8 -*
import imutils
import cv2

img = cv2.imread('/Users/hackerifyouwant/Downloads/index.jpg',cv2.IMREAD_GRAYSCALE)
img = imutils.skeletonize(img,size=(3,3))
cv2.imshow("123",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
