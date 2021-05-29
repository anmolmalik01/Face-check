import numpy as np
import cv2 as cv

predict_image = '' 

people = [ 'Elon Musk', 'Robert Downey' ]

haar_cascade = cv.CascadeClassifier('./data/haer_file.xml')


def face_recognizer():

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    
    # reading from trained model
    face_recognizer.read('./data/model_trained.yml')

    # add for testing
    img = cv.imread(predict_image)

    # converting to gray
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

    for (x,y,w,h) in faces_rect:
        faces_marked = gray[y:y+h,x:x+w]

        # making prediction
        label, confidence = face_recognizer.predict(faces_marked)
        print('Label = ' + people[label] )
        
        # rectangle
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        # putting text below image
        cv.putText(img, str(people[label]), ( x, y+h+30 ), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)

    cv.imshow('Detected Face', img)

    cv.waitKey(0)

    # destroying window on click q
    while(True):
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv.destroyAllWindows()