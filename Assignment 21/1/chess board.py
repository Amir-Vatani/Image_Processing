import numpy as np
import cv2 as cv

chess = np.zeros(640000).reshape(800,800)

for i in range(0,7,2):
    for j in range(0,7,2):
        chess[i*100:(i+1)*100-1, j*100:(j+1)*100-1] = 255
    i = i + 1
    for j in range(1,8,2):
        chess[i*100:(i+1)*100-1, j*100:(j+1)*100-1] = 255
        
cv.imwrite('1\chess_board.jpg', chess)