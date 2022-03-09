import cv2 as cv
import numpy as np

img1 = cv.resize(cv.imread('1.jpg', 0), (300, 400))
img2 = cv.resize(cv.imread('2.jpg', 0), (300, 400))

result = np.zeros((400,1200), dtype="uint8")

result[0:400,0:300] = img1
result[0:400,300:600] = img1 // 2 + img2 // 3
result[0:400,600:900] = img1 // 3 + img2 // 3
result[0:400,900:1200] = img2

cv.imwrite('Result.jpg', result)