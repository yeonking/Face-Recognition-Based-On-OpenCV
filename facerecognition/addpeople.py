# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:17:19 2017

@author: HPq
"""
from tkinter import *
import cv2
import os

yourname=''

root = Tk()
root.title("GetName")
root.geometry('300x300')                 #是x 不是*


l1 = Label(root, text="xls名：")
l1.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()
xls = Entry(root, textvariable = xls_text)
xls_text.set("")
xls.pack()


def take_photo():
    root.destroy()
    cap = cv2.VideoCapture(0)
    os.mkdir("E:/facerecognition/att_faces/orl_faces/%s"%(yourname))
    print("Have created E:/facerecognition/att_faces/orl_faces/%s"%(yourname))
    i=1
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            cv2.imwrite("E:/facerecognition/att_faces/orl_faces/%s/%d.jpg"%(yourname,i),frame)
            print("Have saved to E:/facerecognition/att_faces/orl_faces/%s/%d.jpg"%(yourname,i))
            i=i+1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def on_click():
    global yourname 
    yourname = xls_text.get()
    take_photo()
    
    
    
Button(root, text="submit", command = on_click).pack()
root.mainloop()

