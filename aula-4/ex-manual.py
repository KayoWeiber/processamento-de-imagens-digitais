import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('lena_gray.jpg',0)

# Cálculo do histograma manualmente
hist = np.zeros(256)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        intensidade = img[i,j]
        hist[intensidade] += 1

total_pixels = img.shape[0] * img.shape[1]
prob = hist / total_pixels

#aplicando CDF
cdf = np.zeros(256)
cdf[0] = prob[0]
for i in range(1, 256):
    cdf[i] = cdf[i-1] + prob[i]

#transformanndo
l = 256
transform = np.floor((l-1) * cdf).astype('uint8')

#aplicando a transformação
img_eq = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_eq[i,j] = transform[img[i,j]]

# Exibindo os resultados
plt.figure(figsize=(10, 8))
plt.subplot(2,2,1)
plt.axis('off')
plt.title('Imagem Original')
plt.imshow(img,cmap='gray')

plt.subplot(2,2,2)
plt.title('Histograma Original')
plt.hist(img.ravel(), bins=256)

plt.subplot(2,2,3)
plt.axis('off')
plt.title('Imagem Equalizada')
plt.imshow(img_eq,cmap='gray')

plt.subplot(2,2,4)
plt.title('Histograma Equalizado')
plt.hist(img_eq.ravel(), bins=256)

plt.show()