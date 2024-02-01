import cv2

video = cv2.VideoCapture('babyryan.mp4')

while(video.isOpened()):
    ret,frame=video.read()

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

model = cv2.CascadeClassifier("haarcascade.xml")

faces = model.detectMultiScale(gray_image)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,0,255), 1)

#cv2.rectangle(image, (50,50), (150,150), (0,125,255),1)
cv2.imshow('original image',image)
cv2.imshow('gray_image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()