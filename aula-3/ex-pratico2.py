import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("ft_kayo.jpg",0)
neg =255 - img

plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title("imagem original")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(neg,cmap='gray')
plt.title("Negativo")
plt.axis('off')

plt.subplot(2,2,3)
plt.hist(img.ravel(),bins = 256,range=[0,256])
plt.title('Histograma original')

plt.subplot(2,2,4)
plt.hist(neg.ravel(),bins=256,range=[0,256])
plt.title("Histograma negativo")
plt.show()
