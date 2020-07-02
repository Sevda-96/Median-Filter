import cv2

import numpy as np

# Median Süzgeç
img = cv2.imread('prosthesis_salt_pepper.bmp ')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(img, 5)

# gorntuyu kaydeder
cv2.imwrite('soru4-sonuc.jpg', median)

# orinal ve sonuc goruntuleri gosterir
cv2.imshow("orjinal", img)
cv2.imshow("Sonuc", median)
cv2.waitKey(0)
cv2.destroyAllWindows()
