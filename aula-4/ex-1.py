import cv2
import matplotlib.pyplot as plt

img= cv2.imread("lena_gray.jpg",0)
eq = cv2.equalizeHist(img)

plt.subplot(2,2,1)
plt.axis('off')
plt.title('imagem original')
plt.imshow(img,cmap='gray')

plt.subplot(2,2,2)
plt.title('Histograma Original')
plt.hist(img.ravel(),bins=256)

plt.subplot(2,2,3)
plt.axis('off')
plt.title('imagem equalizada')
plt.imshow(eq,cmap='gray')

plt.subplot(2,2,4)
plt.title('histograma equalizado')
plt.hist(eq.ravel(),bins=256)
plt.show()