import cv2

# import numpy as np


faceCascade = cv2.CascadeClassifier(r"classifier/haarcascade_frontalface_alt.xml")  # xml uzantılı hazır veri setini projeye classifier klasörü oluşturup o klasörün içine aktardım
# cv.CascadeClassifier ile okuyup faceCascade e aktardım


cap = cv2.VideoCapture(0)  # camerayı değişkene aktararak işlemlerde kullandım

while True:
    ret, frame = cap.read()  # sonsuz döngü içinde kamera frame şeklinde okunuyor
    gray = cv2.cvtColor(frame,
                        cv2.COLOR_BGR2GRAY)  # işlemleri hızlandırmak adına kamerayı arka planda gri tonlarına döndürdüm
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)  # cameradan yüzleri daha iyi tanıması için verilmiş özellikleri tanımladım

    for (
    x, y, w, h) in faces:  # yüzü tanıdıktan sonra kare içine alması(kareyi ekrana çizmesi) için bu for u oluşturdum
        cv2.rectangle(frame, (x, y), (x + w, y + h), (120, 32, 200), 3)

    cv2.imshow("video", frame)  # okunan kamera görüntüsünü ekrana yansıtmak için bu kod satırını yazdım

    if cv2.waitKey(1) & 0xFF == ord("q"):  # q'a basıldığında çalışmayı durduruyor
        break

cap.release()
cv2.destroyAllWindows()
