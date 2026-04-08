import cv2
import numpy as np
import matplotlib.pyplot as plt

# carregar imagem
img = cv2.imread("lena.jpg", 0)

# kernel sharpen
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# aplicar filtro
sharp = cv2.filter2D(img, -1, kernel)

# exibir
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Sharpen")
plt.imshow(sharp, cmap='gray')
plt.axis("off")

plt.show()