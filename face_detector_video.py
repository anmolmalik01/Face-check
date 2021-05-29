import cv2 as cv

select_video = ''

def face_detector_video():
    
    video = cv.VideoCapture(select_video)

    haar_cascade = cv.CascadeClassifier('./data/haer_file.xml')
    
    while(True):
        
        # Capture the video frame by frame
        ret, frame = video.read()
        
        # Display the resulting frame
                
        faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
        for (x,y,w,h) in faces_rect:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)


        cv.imshow('frame', frame)
        
        # destroying window on click q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    print('======================= video ready to play =======================')
    video.release()
    cv.destroyAllWindows()
