import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

small = cv2.resize(img_rgb,(64,64))
big = cv2.resize(small,(512,512),interpolation=cv2.INTER_NEAREST)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title('Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(big)
plt.title('baixa amostragem')
plt.axis('off')

plt.show()