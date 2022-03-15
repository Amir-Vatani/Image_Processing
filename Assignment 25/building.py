import cv2 as cv
import numpy as np

img = cv.imread("input/building.tif", 0)

height, width = img.shape
mask1 = [[-1,0,1],
        [-1,0,1],
        [-1,0,1]]

mask2 = [[-1,-1,-1],
        [0,0,0],
        [1,1,1]]
result1 = np.zeros(img.shape)
result2 = np.zeros(img.shape)

for i in range (1, height-1) :
    for j in range(1, width-1) :          
        small_img = img[i-1:i+2, j-1:j+2]
        result1[i,j] = np.sum(small_img * mask1)
        result2[i,j] = np.sum(small_img * mask2)              
        
cv.imwrite("output/building_output1.jpg", result1)
cv.imwrite("output/building_output2.jpg", result2)