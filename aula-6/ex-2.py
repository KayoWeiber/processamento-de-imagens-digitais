import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena_gray.jpg",0)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

mag = np.sqrt(sobelx**2 + sobely**2)
mag =  cv2.convertScaleAbs(mag)

plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.title('SOBEL X')
plt.imshow(cv2.convertScaleAbs(sobelx),cmap='gray')
plt.axis("off")
plt.subplot(1,3,2)
plt.title('SOBEL Y')
plt.imshow(cv2.convertScaleAbs(sobely),cmap='gray')
plt.axis("off")
plt.subplot(1,3,3)
plt.title('MAGNITUDE')
plt.imshow(mag,cmap='gray')
plt.axis("off")
plt.show()
