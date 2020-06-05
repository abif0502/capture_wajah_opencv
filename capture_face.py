''''
ABI FIRMANSYAH
instagram.com/f.abii__
'''

import cv2 # Mengambil Library openCV
import os
import waktu as wk # Mengambil informasi waktu yang telah diformat untuk nama file waktu.py

cam = cv2.VideoCapture(0)
cam.set(3, 640) # mengatur lebar video (pixel)
cam.set(4, 480) # mengatur tinggi video (pixel)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Memasukkan id untuk setiap user/orang
face_id = input('\n Masukkan id user dan tekan (enter) ==>  ')

print("\n [" + wk.waktu() + "] sedang mengambil gambar, tunggu sebentar ...")

count = 0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Menyimpan data foto ke folder dataset
        cv2.imwrite("dataset/Orang." + str(face_id)+ '.' + wk.waktu() + '.' + '(' + str(count)+ ')' + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # ESC untuk exit video
    if k == 27:
        break
    elif count >= 10: # Mengambil 10 foto untuk setiap user
        break


print("\n [" + wk.waktu() + "] sedang keluar dari program ...")
print("\n [" + wk.waktu() + "] pengambilan gambar selesai")
cam.release()
cv2.destroyAllWindows()


