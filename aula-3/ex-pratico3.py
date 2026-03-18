import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("ft_kayo.jpg",0)
gamma=0.5
gamma2 = 2
gama_img = np.array(255*(img/255)**gamma,dtype = 'uint8')
gama_img2 = np.array(255*(img/255)**gamma2,dtype = 'uint8')

plt.subplot(3,3,1)
plt.imshow(img,cmap='gray')
plt.title("imagem original")
plt.axis('off')

plt.subplot(3,3,2)
plt.imshow(gama_img,cmap='gray')
plt.title("gamma")
plt.axis('off')

plt.subplot(3,3,3)
plt.imshow(gama_img2,cmap='gray')
plt.title("gamma2")
plt.axis('off')

plt.subplot(3,3,4)
plt.hist(img.ravel(),bins = 256,range=[0,256])
plt.title('Histograma original')

plt.subplot(3,3,5)
plt.hist(gama_img.ravel(),bins=256,range=[0,256])
plt.title("Histograma gama")

plt.subplot(3,3,6)
plt.hist(gama_img2.ravel(),bins=256,range=[0,256])
plt.title("Histograma gama2")
plt.show()
