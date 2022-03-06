import cv2 as cv
import numpy as np

img = cv.imread('5\heath ledjer.jpg')

img = cv.resize(img, (400, 600))

for i in range(120):
    img[i:i+50, 120-i-1] = 0

for i in range(50):
    img[0:50-i, 120+i-1] = 0

cv.imwrite('5\deceased_heath ledjer.jpg', img)