import cv2
import matplotlib.pyplot as plt

img = cv2.imread("lena.jpg", 0)
blur = cv2.blur(img, (3,3))
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
