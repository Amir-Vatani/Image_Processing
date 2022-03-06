import numpy as np
import cv2 as cv

gradient = np.empty(459000).reshape(765,600)

j=0
for i in range(0,765,3):
    gradient[i:i+3, 0:600] = 255 - j
    if i % 3 == 0 :
        j=j+1

cv.imwrite('6\gradient.jpg', gradient)