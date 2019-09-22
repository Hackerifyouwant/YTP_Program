#-*- coding: utf-8 -*
import cv2
import numpy as np
import imutils
import dlib

#讀圖片
img = cv2.imread('/Users/hackerifyouwant/Downloads/index.jpg')
#用imutils調整圖片大小
img = imutils.resize(img, width=1280)
#dlib的人臉偵測器
detector = dlib.get_frontal_face_detector()
#偵測人臉
face_rects = detector(img,0)
#取出所有偵測結果
for i, d in enumerate(face_rects):
  x1 = d.left()
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()
#以方匡表示人臉
  cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)
#顯示圖像
cv2.imshow("Twicedetector",img)
#cv2.imwrite("/Users/hackerifyouwant/YTP/Twicedetector.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
