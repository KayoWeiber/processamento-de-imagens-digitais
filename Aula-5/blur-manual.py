import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lena.jpg", 0)
#blur = cv2.blur(img, (3,3))

kernel = np.ones((3,3)) / 9

h, w = img.shape
blur = np.zeros_like(img)

for i in range(1, h-1):
    for j in range(1, w-1):
        region = img[i-1:i+2, j-1:j+2]
        blur[i,j] = np.sum(region * kernel)

#se quiser salvar a imagem suavizada...
cv2.imwrite("lena_suavizada.jpg", blur)

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(blur, cmap='gray')
plt.title("Suavizada")
plt.axis("off")

plt.show()
