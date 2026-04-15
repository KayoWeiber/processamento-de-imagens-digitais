import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena_gray.jpg")

kernelSh = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharp = cv2.filter2D(img, -1, kernelSh)
imgsh=sharp
sobelx = cv2.Sobel(imgsh,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(imgsh,cv2.CV_64F,0,1,ksize=3)

mag = np.sqrt(sobelx**2 + sobely**2)
mag =  cv2.convertScaleAbs(mag)

kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=np.float32)

kernely = np.array([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=np.float32)

prewidttx = cv2.filter2D(imgsh,cv2.CV_64F,kernelx)
prewidtty = cv2.filter2D(imgsh,cv2.CV_64F,kernely)
magprewitt = np.sqrt(prewidttx**2 + prewidtty**2)
magprewitt =  cv2.convertScaleAbs(magprewitt)

lap = cv2.Laplacian(imgsh,cv2.CV_64F)
lap_abs = cv2.convertScaleAbs(lap)

plt.figure(figsize=(12,4))
plt.subplot(1,5,1)
plt.title('Original')
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.subplot(1,5,2)
plt.title('Sharpening')
plt.imshow(sharp,cmap='gray')
plt.axis("off")
plt.subplot(1,5,3)
plt.title('SOBEL MAG')
plt.imshow(mag,cmap='gray')
plt.axis("off")
plt.subplot(1,5,4)
plt.title("mag prewitt")
plt.imshow(magprewitt,cmap='gray')
plt.axis("off")
plt.subplot(1,5,5)
plt.title("Laplacian")
plt.imshow(lap_abs,cmap='gray')
plt.axis("off")
plt.show()