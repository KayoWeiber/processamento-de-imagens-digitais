import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', 0)

gauss = cv2.GaussianBlur(img, (5,5), 0)

plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Gaussiano")
plt.imshow(gauss, cmap='gray')
plt.axis('off')

plt.show()