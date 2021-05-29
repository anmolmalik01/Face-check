import cv2 as cv

def face_detector_video_live():  
    video = cv.VideoCapture(0)

    haar_cascade = cv.CascadeClassifier('./data/haer_file.xml')
  
    while(True):
    
        # Capture the video frame by frame
        ret, frame = video.read()
    
        # Display the resulting frame
            
        faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=9)
        for (x,y,w,h) in faces_rect:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        cv.imshow('frame', frame)

        # destroying window on click q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    video.release()
    cv.destroyAllWindows()