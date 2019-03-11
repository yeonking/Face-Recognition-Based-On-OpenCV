# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:35:25 2017

@author: HP
"""

import numpy as np  
import cv2 
import pandas as pd

name=pd.read_csv("name.txt",header=None,sep=";",names=['who','label'])
print(name.head())



model=cv2.face.LBPHFaceRecognizer_create()

model.read("E:/facerecognition/MyFaceLBPHModelnew.xml")



face_cascade = cv2.CascadeClassifier("E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml")  
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")  



faces = face_cascade.detectMultiScale(test,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(test.shape[0],test.shape[1]))  

img=cv2.imread("E:/facerecognition/test/s3_10.pgm")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(img.shape[0],img.shape[1])) 

result_i=model.predict(gray)
result_n=name.who[name.label==result_i[0]][result_i[0]]
sstr=str(result_i[0])+','+str(result_n)+','+str(result_i[1])

if result_i[1]<=95:
    cv2.putText(img, sstr, (2,16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
else:
    cv2.putText(img, "None", (x,y),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
cv2.namedWindow("img",cv2.WINDOW_NORMAL) 
cv2.imshow("img",img)
cv2.waitKey(0)         
 
'''
if len(faces)>0:
    for faceRect in faces:
        x,y,w,h = faceRect
        roi_gray = gray[y:y+h,x:x+w]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5,8,0)
       
        roi_res=cv2.resize(roi_gray,(92,112))
        
        result_i=model.predict(roi_res)
        result_n=name.who[name.label==result_i[0]][result_i[0]]
         
        sstr=str(result_i[0])+','+str(result_n)+','+str(result_i[1])
        
        if result_i[1]<=95:
            cv2.putText(img, sstr, (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)            
        else:
            cv2.putText(img, "None", (x,y),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)                   
        cv2.imshow("recognition(q:exit)", img)
        cv2.waitKey(0)        

    
else:
    print("noface")'''

'''

result_i=model.predict(test)
print(result_i)
    
result_n=name.who[name.label==result_i[0]][result_i[0]]
print(result_n)
'''