import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lena_gray.jpg",0)
gamma=0.5
gama_img = np.array(255*(img/255)**gamma,dtype = 'uint8')

plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title("imagem original")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(gama_img,cmap='gray')
plt.title("Gama")
plt.axis('off')

plt.subplot(2,2,3)
plt.hist(img.ravel(),bins = 256,range=[0,256])
plt.title('Histograma original')

plt.subplot(2,2,4)
plt.hist(gama_img.ravel(),bins=256,range=[0,256])
plt.title("Histograma gama")
plt.show()
