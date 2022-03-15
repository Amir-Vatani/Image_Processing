import cv2 as cv
import numpy as np

img = cv.imread("input/lion.png", 0)

height, width = img.shape
mask = [[0,-1,0],
        [-1,4,-1],
        [0,-1,0]]
result = np.zeros(img.shape)

for i in range (1, height-1) :
    for j in range(1, width-1) :          
        small_img = img[i-1:i+2, j-1:j+2]
        result[i,j] = np.sum(small_img * mask)       
        
cv.imwrite("output/lion_output.jpg", result)