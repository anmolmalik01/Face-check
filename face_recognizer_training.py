import cv2 as cv
import os
import numpy as np


# arrays defined for x, y of training set
features = []
labels = []

# direcory of images
people = [ 'Elon Musk', 'Robert Downey' ]
DIR = './images'

# face detection file
haar_cascade = cv.CascadeClassifier('./data/haer_file.xml')

def create_train():
    for x in people:
        path = os.path.join(DIR, x)
        index = people.index(x)
     

        for img in os.listdir(path):
            # making the location of image
            img_path = os.path.join(path, img)

            # reading image from img_path
            img_array = cv.imread(img_path)

            if img_array is None:
                continue
            
            # converting to gray scale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

            for (x, y, w, h) in face_rect:
                faces_marked = gray[y:y+h, x:x+w]
                features.append(faces_marked)
                labels.append(index)


def train_model():

    create_train()

    X = np.array(features, dtype='object')
    Y = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # trainiAfflekng model
    face_recognizer.train(X, Y)
    print('======================= Training done =======================')

    # saving model to use further
    face_recognizer.save('./data/model_trained.yml')
    np.save('./data/model_features.npy', X)
    np.save('./data/model_labels.npy', Y)
    print('======================= Files saved =======================')
