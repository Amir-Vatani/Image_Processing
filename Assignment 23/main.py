import cv2 as cv
from cv2 import waitKey

def remove_background(img, position) :       
    img2gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _,mask= cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)
    background = cv.bitwise_and(position, position, mask = mask_inv)
    mask_img = cv.bitwise_and(img, img, mask=mask)
    emoji_without_back = cv.add(mask_img ,background)
    
    return emoji_without_back


face_detector = cv.CascadeClassifier("data/haarcascade_frontalface_default.xml")


emoji = cv.imread("img/emoji.png")
eyes_emoji = cv.imread("img/eye.png")
lip_emoji = cv.imread("img/lip.png")

videocap = cv.VideoCapture(0)
key = 0
user_choice = 0

while True :
    ret, frame = videocap.read()
    if ret == False :
        break
    
    # manage user choice  
    if key == 27 : #ese
        break
    elif key == 49 :
        user_choice = 1
    elif key == 50 :
        user_choice = 2
    elif key == 51 :
        user_choice = 3
    elif key == 52 :
        user_choice = 4
        
    face = face_detector.detectMultiScale(frame, 1.2, minNeighbors=5)
    
    for (x, y, w, h) in face :
        face_position = frame[y:y+h, x:x+w]
        
        if user_choice == 1 : # emoji on face
            img = cv.resize(emoji, (w, h))
            emoji_without_back = remove_background(img, face_position)
            
            frame[y:y+h, x:x+h] = emoji_without_back
    
        elif user_choice == 2 : # eye and lip
            eye_detector = cv.CascadeClassifier("data/haarcascade_eye.xml")
            mouth_detector = cv.CascadeClassifier("data/smile.xml")

            eyes = eye_detector.detectMultiScale(face_position, 1.3, 5)
            for (ex, ey, ew, eh) in eyes :
                eye_position = frame[y + ey:y + ey + eh, x + ex:x + ex + ew]
                
                img = cv.resize(eyes_emoji, (ew, eh))
                eye_without_back = remove_background(img, eye_position)
                frame[y + ey:y + ey + eh, x + ex:x + ex + ew] = eye_without_back

            lips = mouth_detector.detectMultiScale(face_position, 1.9, minNeighbors=20)
            for (mx, my, mw, mh) in lips :
                lip_position = frame[y + my:y + my + mh, x + mx:x + mx + mw]
                
                img = cv.resize(lip_emoji, (mw, mh))
                lip_without_back = remove_background(img, lip_position)
                frame[y + my:y + my + mh, x + mx:x + mx + mw] = lip_without_back
        
        elif user_choice == 3 : # checkered face
            sq = cv.resize(frame[y:y+h,x:x+w], (10,10))
            checkered_face = cv.resize(sq, (w, h), interpolation=cv.INTER_NEAREST)
            frame[y:y+h, x:x+h] = checkered_face
            
        elif user_choice == 4 : # flip horizontal
            frame[y:y+h, x:x+h] = face_position[::-1, ::]
            
    cv.imshow('output', frame)
    key = cv.waitKey(10)
    
videocap.release()