from email.mime import image
import numpy as np
import cv2 as cv

images = []

for i in range(4) :
    Result = 0
    for j in range(5) :
        Result = Result + cv.imread(f'img/{i+1}/{j+1}.jpg', 0) // 5
    
    images.append(Result)

final = np.zeros((2000, 2000), dtype=np.uint8)

final[0:1000, 0:1000] = images[0]
final[0:1000, 1000:2000] = images[1]
final[1000:2000, 0:1000] = images[2]
final[1000:2000, 1000:2000] = images[3]

cv.imwrite('Result.jpg', final)