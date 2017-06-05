import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('/home/someone/Desktop/OPENCV/3D-Matplotlib.png')

img2 = cv2.imread('/home/someone/Desktop/OPENCV/mainsvmimage.png')

img3 = cv2.imread('/home/someone/Desktop/OPENCV/mainlogo.png')

#add = img1 + img2
#add = cv2.add(img1,img2)
#add = cv2.addWeighted(img1,0.4,img2,0.6,0) #gamle value


rows,cols,channels = img3.shape
roi = img1[0:rows,0:cols]
img3gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, add = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)
# THRESH_BINARY .. THRESH_BINARY_INV .. THRESH_TRUNC .. THRESH_TOZERO .. THRESH_TOZERO_INV



cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows 