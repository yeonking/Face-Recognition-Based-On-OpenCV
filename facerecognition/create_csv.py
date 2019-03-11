# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:51:06 2017

@author: HP
"""
 
import os.path  

if __name__ == "__main__":  
  
    #if len(sys.argv) != 2:  
    #    print "usage: create_csv <base_path>"  
    #    sys.exit(1)  
  
    #BASE_PATH=sys.argv[1]  
    BASE_PATH="E:/facerecognition/att_faces/orl_faces/"  
      
    SEPARATOR=";"  
  
    fh = open("at.txt",'w')
    fn = open("name.txt",'w') 
  
    label = 0 
    for dirname, dirnames, filenames in os.walk(BASE_PATH):  
        for subdirname in dirnames:  
            subject_path = os.path.join(dirname, subdirname)
            print("%s%s%d" % (subdirname, SEPARATOR, label))
            fn.write(subdirname)  
            fn.write(SEPARATOR)  
            fn.write(str(label))  
            fn.write("\n")
            for filename in os.listdir(subject_path):  
                abs_path = "%s/%s" % (subject_path, filename)  
                print("%s%s%d" % (abs_path, SEPARATOR, label))  
                fh.write(abs_path)  
                fh.write(SEPARATOR)  
                fh.write(str(label))  
                fh.write("\n")        
            label = label + 1  
    fn.close()
    fh.close()  