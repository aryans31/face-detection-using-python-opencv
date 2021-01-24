import cv2
import os   
import numpy as np
from PIL import Image

recognizer =  cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

path='dataSet'

def getImagesWithID(path):
    print(" \n\n TRAINING STARTED\n\n")

    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    print(imagePaths)
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split(".")[2])
        faces.append(faceNp)
        print(faces)
        print(ID)
        IDs.append(ID)
        print(IDs)
        cv2.imshow("training in progress",faceNp)
        cv2.waitKey(100)
    return IDs,faces    

Ids,faces = getImagesWithID(path)
print(recognizer)
recognizer.train(faces,np.array(Ids))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()









