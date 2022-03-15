import cv2 as cv
import numpy as np

# img = cv.imread("input/flower_input.jpg", 0)

# height, width = img.shape
# mask = np.ones((15,15)) / 225
# result = np.zeros(img.shape)

# for i in range (7, height-7) :
#     for j in range(7, width-7) :          
#         small_img = img[i-7:i+8, j-7:j+8]
#         if img[i,j] < 200 :
#             result[i,j] = np.sum(small_img * mask)
#         else :
#             result[i,j] = img[i,j]        
        
# cv.imwrite("output/flower_output.jpg", result)

video_cap = cv.VideoCapture(0)

while True:
    ret,frame = video_cap.read()
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    detect = frame[180:300,270:390]
      
    if ret == False:
        break
    
    cv.rectangle(frame,(270,180), (390,300), (0, 0, 0),2)
    
    cv.imshow('output', frame)