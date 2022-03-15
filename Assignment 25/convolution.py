import cv2 as cv
import numpy as np

def convolution(img, row_mask, col_mask, value_mask) :
    mask = np.ones((row_mask,col_mask)) * value_mask
    height, width = img.shape
    result = np.zeros(img.shape)
    
    for i in range (row_mask//2, height - row_mask//2) :
        for j in range(col_mask//2, width - col_mask//2) :          
            small_img = img[i - row_mask//2:i + row_mask//2 + 1, j - col_mask//2:j + col_mask//2 + 1]
            result[i,j] = np.sum(small_img * mask) 
        
    return result

img = cv.imread("input/flower_input.jpg", 0)

result = convolution(img, 15, 15, 1/225)   
cv.imwrite('output.jpg', result)
cv.waitKey()