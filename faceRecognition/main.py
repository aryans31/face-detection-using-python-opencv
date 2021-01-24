import cv2
import datetime
import mysql.connector

# recognizer and classifier and vid capture
facedetect = cv2.CascadeClassifier("/home/eclipse31/aryan/vscode/python/faceRecognition/haarcascade_frontalface_alt.xml")
recognizer =  cv2.face.LBPHFaceRecognizer_create()
recognizer.read("/home/eclipse31/aryan/vscode/python/faceRecognition/recognizer/trainingData.yml")
font=cv2.FONT_HERSHEY_COMPLEX
cam=cv2.VideoCapture(0)

# my sql connector
print("My sql connector version  "+ format(mysql.connector.__version__))
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="student")
mycursor=mydb.cursor()
# get function
def getProfile(id):
    cmd= """select * from information where id = %s"""
    mycursor.execute(cmd, (id,))
    result = mycursor.fetchall()
    profile=None
    for row in result:
        profile=row
        print(profile)
    return profile
text=str(datetime.datetime.now())
def present(id):
    cmmd="""update information set time = %s where id = %s AND time IS NULL"""
    mycursor.execute(cmmd, (text,id))
    mydb.commit()
    
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray, 1.2,5)

    for(x,y,w,h) in faces:
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(id,conf)
        profile=getProfile(id)
        if(conf<70):
            if(profile!=None ):
             present(id)
             cv2.rectangle(im,(x,y),(x+w,y+h),(0,225,0),2)
             cv2.putText(im,str(profile[0]), (x,y+h+40),font, 1, (32,32,32),2)
             cv2.putText(im,str(profile[1]), (x,y+h+80),font, 1, ( 32,32,32),2)
             cv2.putText(im,"SUCCESSFUL", (x,y+h+140),font, 1.5, (0, 225,0),3)
             cv2.putText(im,text, (50,50),font, 0.5, ( 0,0,0),2)

        else:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,225),2)
            cv2.putText(im,"UNKNOWN", (x-40,y-30),font, 1.5, (0,0,225),3)
            cv2.putText(im,"NO MATCH FOUND!!!!", (x-160,y+h+50),font, 1.5, (0,0,225),3)
          
    cv2.imshow("image",im)
    if(cv2.waitKey(1)& 0xff==ord("q")):
        break
    
cam.release()
cv2.destroyAllWindows()
mydb.close()
print("code successful")