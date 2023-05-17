import cv2

import numpy as np


cap = cv2.VideoCapture(1)  # camerayı değişkene aktararak işlemlerde kullandım

yukseklik = 600
genislik = 720


i=0
while True:
    ret, frame = cap.read()  # sonsuz döngü içinde kamera frame şeklinde okunuyor
    """gray = cv2.cvtColor(frame,
                        cv2.COLOR_BGR2GRAY)  """# işlemleri hızlandırmak adına kamerayı arka planda gri tonlarına döndürdüm

    frame = cv2.resize(frame, (genislik, yukseklik))

    cv2.imwrite('kang' + str(i) + '.jpg', frame) # kameradan aldığımız görüntüleri kayıt etmek için bu satır oluşturuldu
    i += 1

    cv2.imshow("video", frame)  # okunan kamera görüntüsünü ekrana yansıtmak için bu kod satırını yazdım

    if cv2.waitKey(1) & 0xFF == ord("q"):  # q'a basıldığında çalışmayı durduruyor
        break

cap.release()
cv2.destroyAllWindows()

