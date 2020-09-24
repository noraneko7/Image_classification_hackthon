#目、顔の位置摘出

import cv2
face_cascade_path = './drive/My Drive/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = './drive/My Drive/opencv-master/data/haarcascades/haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
img=cv2.imread('saruman.jpg',cv2.COLOR_BGR2GRAY)
src_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(src_gray)
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face = img[y: y + h, x: x + w]
    face_gray = src_gray[y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
cv2.imwrite('saruman2.jpg', img)