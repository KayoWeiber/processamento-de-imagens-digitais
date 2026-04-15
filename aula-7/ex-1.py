import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena_gray.jpg")

kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=np.float32)

kernely = np.array([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=np.float32)

prewidttx = cv2.filter2D(img,cv2.CV_64F,kernelx)
prewidtty = cv2.filter2D(img,cv2.CV_64F,kernely)
prewidttx_abs = cv2.convertScaleAbs(prewidttx)
prewidtty_abs = cv2.convertScaleAbs(prewidtty)

lap = cv2.Laplacian(img,cv2.CV_64F)
lap_abs = cv2.convertScaleAbs(lap)

plt.figure(figsize=(10,4))
plt.subplot(1,4,1)
plt.title('Original')
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.subplot(1,4,2)
plt.title("Prewitt x")
plt.imshow(prewidttx_abs,cmap='gray')
plt.axis("off")
plt.subplot(1,4,3)
plt.title("Prewitt y")
plt.imshow(prewidtty_abs,cmap='gray')
plt.axis("off")
plt.subplot(1,4,4)
plt.title("Laplacian")
plt.imshow(lap_abs,cmap='gray')
plt.axis("off")
plt.show()