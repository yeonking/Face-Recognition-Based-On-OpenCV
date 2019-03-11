# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:21:29 2017

@author: HP
"""

import numpy as np  
import cv2 
import pandas as pd
import os

def updatemymodel(yourname):

    BASE_PATH="E:/facerecognition/att_faces/orl_faces/%s/"%(yourname)  
          
    SEPARATOR=";"  
      
    fh = open("atnew.txt",'w')
    fn = open("name.txt",'a')
    
    at=pd.read_csv("name.txt",header=None,sep=";")
    print(at[1].max()) 
    
     
    label = at[1].max()+1
    print("%s%s%d" % (BASE_PATH[39:-1], SEPARATOR, label))
    fn.write(BASE_PATH[39:-1])
    fn.write(SEPARATOR)
    fn.write(str(label))
    fn.write("\n")
    for filename in os.listdir(BASE_PATH):
        abs_path = "%s/%s" % (BASE_PATH, filename)
        print("%s%s%d" % (abs_path, SEPARATOR, label))
        fh.write(abs_path)
        fh.write(SEPARATOR)
        fh.write(str(label))
        fh.write("\n")
        
    fn.close()
    fh.close() 
     
    
    at=pd.read_csv("atnew.txt",header=None,sep=";")
    
    images=[]
    labels=[]
    
    #print(at.iat[1,0])
    
    for i in range(len(at)):
        img=cv2.imread(at.iat[i,0])
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        gray = cv2.resize(gray,(92,112))
        images.append(gray)
        labels.append(at.iat[i,1])
    
    
    
    images=np.array(images)
    labels=np.array(labels)
    
    model=cv2.face.LBPHFaceRecognizer_create()
    model.read("E:/facerecognition/MyFaceLBPHModelnew.xml")
    model.update(images,labels)
    model.write("MyFaceLBPHModelnew.xml")
    
print("completed update")