import cv2 
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
level = 8

quant = np.floor(gray/(256/level))*(256/level) + (256/(2*level))
quant = quant.astype(np.uint8)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray', vmin=0, vmax=255)
plt.title('Original em cinza')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(quant, cmap='gray', vmin=0, vmax=255)
plt.title('Quantizada')
plt.axis('off')
plt.show()