import cv2
import matplotlib.pyplot as plt
import numpy as np  

# carregar imagem
img = cv2.imread("teste2.jpg", 0)

media = cv2.blur(img, (3,3))
gauss = cv2.GaussianBlur(img, (5,5), 0)
# kernel sharpen
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharp = cv2.filter2D(img, -1, kernel)

plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis("off")

plt.subplot(2,2,2)
plt.title("Média")
plt.imshow(media, cmap='gray')
plt.axis("off")

plt.subplot(2,2,3)
plt.title("Gaussiano")
plt.imshow(gauss, cmap='gray')
plt.axis("off")

plt.subplot(2,2,4)
plt.title("Sharpen")
plt.imshow(sharp, cmap='gray')
plt.axis("off")

plt.show()