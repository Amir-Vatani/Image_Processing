import cv2 as cv
import numpy as np

img1 = cv.imread('board - origin.bmp', 0)
img2 = cv.imread('board - test.bmp', 0)

img2 = img2[::,::-1] #rotate

cv.imwrite('Result.jpg', cv.absdiff(img1, img2))  # cv.subtract(img1, img2)