import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena_gray.jpg')
edges = cv2.Canny(img, 20, 100)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edges')
plt.axis('off')

plt.show()