import argparse
import cv2
import matplotlib.pyplot as plt
from imutils.perspective import four_point_transform


webcam = cv2.VideoCapture(0)

while True :
    ret,frame = webcam.read()

    if not ret:
        break

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred_img = cv2.GaussianBlur(gray_img , (7,7), 3)

    threshod = cv2.adaptiveThreshold(blurred_img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 11 ,2)

    contours = cv2.findContours(threshod, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

    contours = contours[0]
    contours = sorted(contours , key = cv2.contourArea , reverse = True)

    sudoku_contour = None

    for contour in contours:
        epsilon = 0.15 * cv2.arcLength(contour , True)
        approx = cv2.approxPolyDP(contour , epsilon , True)
                                
        if len(approx) == 4:
            sudoku_contour = approx
            break

    if sudoku_contour is None :
        cv2.putText(frame, "Not found", (10, 60), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 
    else:
        result = cv2.drawContours(frame , [sudoku_contour] , -1 ,(0,255,0) , 8)
        # cv2.imwrite(args.output, sudoku)
    
    cv2.imshow('output', frame)
    key = cv2.waitKey(10)
    if key == 27 : #esc
        break
    if key == ord('s') : #save
        sudoku = four_point_transform(frame, sudoku_contour.reshape(4,2))
        cv2.imwrite("output/webcam_result.jpg", sudoku)