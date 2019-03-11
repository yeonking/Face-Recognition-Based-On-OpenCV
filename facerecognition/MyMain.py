# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:45:25 2017

@author: HP
"""

import cv2
import numpy as np  
import pandas as pd
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
from updatemodel import updatemymodel

name=pd.read_csv("name.txt",header=None,sep=";",names=['who','label'])
model=cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier("E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml")  
yourname=''   

root = Tk()

root.geometry('300x250')

label = Label(root, 
              wraplength=250,
              text = 'If my programm cannot recognize you , you can enter your name in the input box and press submit button to tell my programm who you are.And then press p to take several photoes to introduce yourself to my programm.')
label.pack()

label2 = Label(root,
              text = 'Name:')
label2.pack(anchor=W,padx=20)

xls_text = StringVar()
xls = Entry(root, textvariable = xls_text)
xls_text.set("")
xls.pack(fill=X,padx=20)



def take_photo():
    cap = cv2.VideoCapture(0)
    if not os.path.exists("E:/facerecognition/att_faces/orl_faces/%s"%(yourname)):
        os.mkdir("E:/facerecognition/att_faces/orl_faces/%s"%(yourname))
        print("Have created E:/facerecognition/att_faces/orl_faces/%s"%(yourname))
    i=1
    while(1):
        # get a frameq
        ret, frame = cap.read()
        img=frame
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(img.shape[0],img.shape[1]))  
        if len(faces)>0:
            for faceRect in faces:
                x,y,w,h = faceRect            
                roi_gray = gray[y:y+h,x:x+w]  
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5,8,0)
            if cv2.waitKey(1) & 0xFF == ord('p'):
                cv2.imwrite("E:/facerecognition/att_faces/orl_faces/%s/%d.jpg"%(yourname,i),roi_gray)
                print("Have saved to E:/facerecognition/att_faces/orl_faces/%s/%d.jpg"%(yourname,i))
                i=i+1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            updatemymodel(yourname)
            break
        cv2.imshow("recognition(Press p:take photo,q:exit)", img)        
    cap.release()
    cv2.destroyAllWindows()


def on_click():
    global yourname
    yourname = xls_text.get()
    if len(yourname)>0:
        take_photo()
    
def recognization():
    
    model.read("E:/facerecognition/MyFaceLBPHModelnew.xml")

    #调用摄像头
    cap = cv2.VideoCapture(0)
     
    #摄像头开始获取图像并检测人脸
    i=1
    while(1):
        # get a frameq
        ret, frame = cap.read()
        img=frame
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(img.shape[0],img.shape[1]))  
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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow("recognition(q:exit)", img)        
    cap.release()
    cv2.destroyAllWindows()

    
    
b1=Button(root, text="Begin Recognition", command = recognization)
b1.pack(side=LEFT)
b1.place_configure(x=20,y=170)

b2=Button(root, text="submit", command = on_click)
b2.pack(anchor=SE)
b2.place_configure(x=150,y=170)

root.mainloop()





'''
#调用摄像头
cap = cv2.VideoCapture(0)
print("diaoyong")
#调用人脸检测模型
face_cascade = cv2.CascadeClassifier("E:/facerecognition/data/haarcascades/haarcascade_frontalface_default.xml")  
#读取姓名库
name=pd.read_csv("name.txt",header=None,sep=";",names=['who','label'])

#摄像头开始获取图像并检测人脸
while(1):
    # get a frame
    ret, frame = cap.read()
    img=frame
    print(type(img))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(img.shape[0],img.shape[1]))  
    if len(faces)>0:
        for faceRect in faces:
            x,y,w,h = faceRect            
            roi_gray = gray[y:y+h,x:x+w]  
            roi_color = img[y:y+h,x:x+w]
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5,8,0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.imshow("recognition(Press 'q' to exit!)", img)
    cv2.imwrite('temp.pgm',img)
    bm = PhotoImage(file = 'temp.pgm')    
    label2 = Label(root, image = bm)
    label2.bm = bm
    label2.pack()
cap.release()
cv2.destroyAllWindows()'''

root.mainloop()    
    



