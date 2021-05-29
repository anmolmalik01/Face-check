import cv2 as cv
 
select_image = ''

haar_cascade = cv.CascadeClassifier('./data/haer_file.xml')


# Display the resulting frame

def face_detector_image():

    image = cv.imread(select_image)
    
    faces_rect = haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=9)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(image, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    print('======================= image ready for showing =======================')

    cv.imshow('Image', image)

    cv.waitKey(0)

    # destroying window on click q
    while(True):
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv.destroyAllWindows()

