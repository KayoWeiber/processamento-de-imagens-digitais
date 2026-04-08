import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena_gray.jpg",0)

kernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype = np.float32)

sobelx = cv2.filter2D(img,-1,kernel)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(img,cmap='gray')
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Sobel x")
plt.imshow(sobelx,cmap='gray')
plt.axis("off")

plt.show()