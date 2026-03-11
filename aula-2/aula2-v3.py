import cv2
img = cv2.imread('lena.jpg')
print('Dimensão da imagem:', img.shape)
print(img.dtype)
print(img[100,100] )

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print('Dimensão da imagem em cinza:', gray.shape)
print(gray[100,100] )