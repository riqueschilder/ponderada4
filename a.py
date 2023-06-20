import cv2
import os

video_capture = cv2.VideoCapture('arsene.mp4')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if not os.path.exists('detected_faces'):
    os.makedirs('detected_faces')

count = 0 

while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]  
        cv2.imwrite(f'detected_faces/face{count}.jpg', face)  
        count += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()