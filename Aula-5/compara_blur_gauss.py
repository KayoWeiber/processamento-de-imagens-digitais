import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', 0)

media = cv2.blur(img, (3,3))
gauss = cv2.GaussianBlur(img, (3,3), 0)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Média")
plt.imshow(media, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Gaussiano")
plt.imshow(gauss, cmap='gray')
plt.axis('off')

plt.show()