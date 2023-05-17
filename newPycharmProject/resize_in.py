import cv2

import numpy as np


resim = cv2.imread("kang33.jpg")

cv2.imshow("noresize", resim)

yukseklik = 366
genislik = 640


resim = cv2.resize(resim, (genislik, yukseklik))
cv2.imshow("Termal", resim)


cv2.waitKey(0)