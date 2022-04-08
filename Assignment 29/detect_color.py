import cv2 as cv
import numpy as np

video_cap = cv.VideoCapture(0)

while True:
    ret,frame = video_cap.read()

    detect_area = frame[180:300,250:350]
      
    if ret == False:
        break
    
    B, G, R = cv.split(frame)
    
    kernel = np.ones((25,25),np.float32)/625
    filter_frame = cv.filter2D(frame, -1, kernel)
    
    filter_frame[180:300,250:350] = detect_area
    
    target = filter_frame[180:300,250:350]
    B_t, G_t, R_t = cv.split(target)
    
    alpha = 3
    beta = 0
    R_t = cv.convertScaleAbs(R_t, alpha=alpha, beta=beta)
    G_t = cv.convertScaleAbs(G_t, alpha=alpha, beta=beta)
    B_t = cv.convertScaleAbs(B_t, alpha=alpha, beta=beta)
    R_avg = round(np.average(R_t))
    G_avg = round(np.average(G_t))
    B_avg = round(np.average(B_t))    
    
    if R_avg<140 and G_avg<200 and B_avg>200 :
        cv.putText(filter_frame, "Blue", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    elif R_avg>200 and G_avg<140 and B_avg<120 :
        cv.putText(filter_frame, "Red", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    elif R_avg<140 and G_avg>200 and B_avg<200 :
        cv.putText(filter_frame, "Green", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
        
    elif R_avg>220 and G_avg>220 and B_avg>220 :
        cv.putText(filter_frame, "White", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 
    elif 80<R_avg<170 and 80<G_avg<170 and 80<B_avg<170 :
        cv.putText(filter_frame, "Gray", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    elif R_avg<80 and G_avg<80 and B_avg<80 :
        cv.putText(filter_frame, "Black", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
        
    
    elif R_avg>200 and G_avg<120 and B_avg>200 :
        cv.putText(filter_frame, "Magenta", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    elif R_avg>200 and G_avg>200 and B_avg<140 :
        cv.putText(filter_frame, "Yellow", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    elif R_avg<40 and G_avg>200 and B_avg>200 :
        cv.putText(filter_frame, "Cyan", (10, 60), cv.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
        
    cv.rectangle(frame,(250,180), (350,300), (0, 255, 0),2)
    cv.imshow('output', filter_frame)
    
    key = cv.waitKey(10)
    if key == 27 : #esc
        break