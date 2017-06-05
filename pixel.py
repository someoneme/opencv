import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('/home/someone/Pictures/aa.png')
rows,cols,c = img.shape

for i in range(rows):
    for j in range(cols):
        #k = x[i,j]
        print img[i,j]