import cv2 as cv
import numpy as np

img = cv.imread('4/4.jpg', 0)

height, width = img.shape
res = np.zeros(width*height).reshape(height,width)

for i in range(height):
    for j in range(width):
        if img[i][j] < 120 :
            res[i][j] = 0
        else :
            res[i][j] = img[i][j]

cv.imwrite('4/result.jpg', res)