# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:05:13 2017

@author: HP
"""
import numpy as np  
import cv2 

face_cascade = cv2.CascadeClassifier("E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml")  
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")  
#face_cascade.load('E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread("E:/facerecognition/test/Eddie_10.jpg")  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 


print(gray.shape)

 
          
faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(img.shape[0],img.shape[1]))  

 
if len(faces)>0:  
    for faceRect in faces:  
        x,y,w,h = faceRect
        roi_gray = gray[y:y+h,x:x+w]  
        roi_color = img[y:y+h,x:x+w]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5,8,0)  
  
  
  
#        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,1,cv2.CASCADE_SCALE_IMAGE,(2,2))  
#        for (ex,ey,ew,eh) in eyes:  
#            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)  
print(roi_gray.shape) 
             
cv2.namedWindow("img",cv2.WINDOW_NORMAL) 
cv2.imshow("img",roi_color)
cv2.waitKey(0) 