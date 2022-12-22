import cv2
import numpy as np 
import face_recognition
import os
from datetime import datetime
import pyrebase

path = 'photos'
images = []
classNames =[]
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


#encodings :-> 
def findEncodings(imges):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList 

encodeListKnown = findEncodings(images)
print('ENCODING COMPLETE')


cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS= cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCurrent = face_recognition.face_locations(imgS)
    encodeCurrent = face_recognition.face_encodings(imgS ,faceCurrent)

    for encodeFace,faceLoc in zip(encodeCurrent,faceCurrent):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            ExistingStudent()
        else:
            messagebox.showerror("Error", "Not found any valid data")
