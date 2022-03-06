import cv2 as cv
import numpy as np

img = cv.imread('3/3.jpg', 0)

height, width = img.shape
res = np.zeros(width*height).reshape(height,width)

for i in range(height):
    for j in range(width):
        res[i][j] = img[height-i-1][j]

cv.imwrite('3/result.jpg', res)