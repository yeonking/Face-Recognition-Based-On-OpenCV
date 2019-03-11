# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:59:22 2017

@author: HP
"""

import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml")  
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")  
#face_cascade.load('E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml')

while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    img=frame
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(img.shape[0],img.shape[1]))  
    if len(faces)>0:
        for faceRect in faces:
            x,y,w,h = faceRect            
            roi_gray = gray[y:y+h,x:x+w]  
            roi_color = img[y:y+h,x:x+w]
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("jin.jpg",frame)
        print("save")
        break
    cv2.imshow("c",img)

cap.release()
cv2.destroyAllWindows()
