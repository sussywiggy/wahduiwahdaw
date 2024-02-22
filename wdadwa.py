import cv2

video = cv2.VideoCapture('babyryan.mp4')
face_detection = cv2.CascadeClassifier("haarcascade.xml")

while True:
    ret, frame = video.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(frame_gray)
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            face = frame[y:y+h, x:x+w]
            face = cv2.resize(face, dsize=(0,0),fx=0.05,fy=0.2)
            face = cv2.resize(face,(w,h),interpolation=cv2.INTER_AREA)
            frame[y:y+h,x:x+w] = face
           # cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),3)
    cv2.imshow('video',frame)
    k = cv2.waitKey(30)
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()