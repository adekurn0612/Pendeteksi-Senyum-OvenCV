Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #memanggil library numpy ke np
... import numpy as np
... #memanggil library cv2
... import cv2
... 
... cam = cv2.VideoCapture(0) #mendefenisilkankamera
... #mendefenisikan file xml muka
... face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
... #mendefenisikan file xml mata
... eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
... #mendefensisikan file xml smile
... smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
... while True:
...     #membuka kamera,mengatur gray dan value gray untuk face
...     ret, img = cam.read()
...     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
...     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
...     #mendeteksi muka
...     for (x,y,w,h) in faces:
...         #menggunakan kotak warnah blue(dialmbil dari nilai bgr) dengan ketebalan 2 px
...         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
...         #mendefenisikan roi grai
...         roi_gray = gray[y:y+h, x:x+w]
...         #mendefenisikan roi color
...         #roi gray dan ccolor digunakan untuk menentukan rumus untuk mendeteksi objek yang value akan di masukan nanti
...         roi_color = img[y:y+h, x:x+w]
...         Cface = [(w/2+x),(h/2+y)]
...         print (str(Cface[0])+","+str(Cface[1]))
...         #menggunakan file xml eye dan menenttukan value dari roi gray untuk mata
...         eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
...         #mendetekdi mata
...         for (ex,ey,ew,eh) in eyes:
...             #mendeteksi mata menggunakan kotak berwarnah hijau(diambil dari nilai bgr) dan ketebalan 2  px
...             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            #menggunakan file xml smile dan menenttukan value dari roi gray untuk smile
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (ex,ey,ew,eh) in smiles:
            #mendeteksi smile menggunakan kotak berwarnah merah(diambil dari nilai bgr) dan ketebalan 2  px
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow('frame',img)
    if cv2.waitKey(1)   &   0xFF == ord('q'): break
cam.release()
