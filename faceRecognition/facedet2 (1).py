import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
path='img'
mylist=os.listdir('img') 
print(mylist)
images =[]
allname=[]
for name in mylist:
   curimg=cv2.imread(f'{path}/{name}')
   images.append(curimg)
   allname.append(os.path.splitext(name)[0])

encoding=[]
for image in images:
   image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
   encode=face_recognition.face_encodings(image)[0]
   encoding.append(encode)
print("encoding complete")
cap=cv2.VideoCapture(0)

while True:

       success, img = cap.read() 
       img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
       loccam=face_recognition.face_locations(img)
      
       encodecam=face_recognition.face_encodings(img,loccam)
   
       for face,enco in zip(loccam,encodecam):
              matches=face_recognition.compare_faces(encoding,enco)
              fdist=face_recognition.face_distance(encoding,enco)
              matchindex=np.argmin(fdist)
              
              if matches[matchindex]:
                     name=allname[matchindex]
                     print(name)
                     y1,x2,y2,x1=face
                     cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
                     cv2.putText(img,name,(x1,y1),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    
       cv2.imshow("face by Abhishek",img)
       cv2.waitKey(1)
