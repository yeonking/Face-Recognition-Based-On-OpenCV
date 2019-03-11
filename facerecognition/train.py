# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:25:01 2017

@author: HP
"""

import numpy as np  
import cv2 
import pandas as pd

at=pd.read_csv("at.txt",header=None,sep=";")

#print(at.head(20))

#print(at.size)

images=[]
labels=[]

#print(at.iat[1,0])

for i in range(len(at)):
    img=cv2.imread(at.iat[i,0])
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    images.append(gray)
    labels.append(at.iat[i,1])



images=np.array(images)
labels=np.array(labels)

model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
model.write("MyFaceLBPHModelnew.xml")

print("end")