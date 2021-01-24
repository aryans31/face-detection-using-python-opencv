import cv2
import numpy as np
import mysql.connector

print("My sql connector version  "+ format(mysql.connector.__version__))
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="student")
mycursor=mydb.cursor()

mycursor.execute("select * from information ") 
for row in mycursor:
     print(row)
     
# input name and roll no
name=input('enter user name  ')
id=input('enter rollno ')
ob=(id,name)
cmd="insert into information(id,name)values(%s,%s)"
mycursor.execute(cmd,ob)
mydb.commit()
mydb.close()

# classifier and vid capture
facedetect = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cam=cv2.VideoCapture(0)
sampleNum=0

while 1 :
    ret,img=cam.read()
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(grey,1.3,5)

    for(x,y,h,w) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/User."+str(name)+"."+str(id)+"."+str(sampleNum)+".jpg",grey[y:y+h,x:x+w])
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
        font=cv2.FONT_HERSHEY_COMPLEX
        img=cv2.putText(img, name, (x,y), font, 1, (0 , 225, 0), 1, cv2.LINE_AA )
        cv2.waitKey(100)

    cv2.imshow("frame",img)
    cv2.waitKey(1)
    if(sampleNum>35):
       break
cam.release()
cv2.destroyAllWindows()

print("code successful")



    
    
   
   