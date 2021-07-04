import cv2

img = cv2.imread('../graphics/br-pixel.png')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gambar Asli', img)
cv2.imshow('Gambar grey', grey)

cv2.waitKey(0)
cv2.destroyAllWindows()
