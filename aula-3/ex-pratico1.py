import cv2
import matplotlib.pyplot as plt

img = cv2.imread("ft_kayo.jpg",0)

plt.imshow(img,cmap='gray')
plt.axis('off')

plt.figure()
plt.hist(img.ravel(),bins=256,range=[0,256])
plt.show()