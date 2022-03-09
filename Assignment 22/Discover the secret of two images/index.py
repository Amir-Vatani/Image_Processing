import numpy as np
import cv2

img1 = cv2.imread('a.tif', 0)
img2 = cv2.imread('b.tif', 0)

cv2.imwrite('result.jpg', img2 - img1)
