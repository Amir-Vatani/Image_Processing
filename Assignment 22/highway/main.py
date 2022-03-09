import cv2 as cv
import numpy as np

images = []
Result = 0
for i in range(1,14) :
    Result = Result + cv.imread(f'img\h{i}.jpg', 0) // 14

cv.imwrite('Result.jpg', Result)