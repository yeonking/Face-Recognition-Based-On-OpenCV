# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:15:10 2017

@author: HP
"""

import numpy as np  
import cv2 
import os

face_cascade = cv2.CascadeClassifier("E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml")  

i=1
j=1
while(os.path.exists("E:/facerecognition/att_faces/orl_faces/Eddie/%d.jpg"%(i))):
    img=cv2.imread("E:/facerecognition/att_faces/orl_faces/Eddie/%d.jpg"%(i))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(img.shape[0],img.shape[1]))  
    print("begin if",i)
    if len(faces)>0:
        print("begin for",i)
        for faceRect in faces:
            print("in for",i)
            x,y,w,h = faceRect            
            roi_gray = gray[y:y+h,x:x+w]  
            roi_color = img[y:y+h,x:x+w]
            cv2.imwrite("E:/facerecognition/att_faces/orl_faces/Eddie/%d.jpg"%(i),roi_gray)
            j=j+1
    i=i+1