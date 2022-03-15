import cv2 as cv
import numpy as np

def convolution(img, row_mask, col_mask, value_mask) :
    mask = np.ones((row_mask,col_mask)) * value_mask
    height, width = img.shape
    result = np.zeros(img.shape)
    
    for i in range (row_mask//2, height - row_mask//2) :
        for j in range(col_mask//2, width - col_mask//2) :          
            small_img = img[i - row_mask//2:i + row_mask//2 + 1, j - col_mask//2:j + col_mask//2 + 1]
            # result[i,j] = img[i,j]
        
    return result

video_cap = cv.VideoCapture(0)

while True:
    ret,frame = video_cap.read()
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    detect_area = frame[180:300,250:350]
      
    if ret == False:
        break
    
    kernel = np.ones((25,25),np.float32)/625
    filter_frame = cv.filter2D(frame, -1, kernel)
    
    filter_frame[180:300,250:350] = detect_area
    
    target = np.average(filter_frame[180:300,250:350])
    if target <= 85 :
        cv.putText(filter_frame, "Black", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 
    elif target > 85 and target <= 150 :
        cv.putText(filter_frame, "Gray", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    elif target > 150 :
        cv.putText(filter_frame, "White", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
        
    cv.rectangle(frame,(250,180), (350,300), (0, 255, 0),2)
    cv.imshow('output', filter_frame)
    
    key = cv.waitKey(10)
    if key == 27 : #esc
        break