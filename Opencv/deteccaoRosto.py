import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haars/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

while(camera.isOpened()):
    ret, img = camera.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w , y+h), (255,0,0), 3)
        roi_gray= gray[y:y+h, x:x+w]
        roi_color= img[y:y+h, x:x+w]

    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
