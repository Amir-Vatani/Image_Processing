import cv2 as cv
import random

img = cv.imread('chess pieces.jpg', 0)
height, width = img.shape

for i in range(1000) :
    noise = random.randint(100, 200)
    position_x = random.randint(0, height-1)
    position_y = random.randint(0, width-1)
    
    img[position_x][position_y] = noise
 
cv.imwrite('result.jpg', img)