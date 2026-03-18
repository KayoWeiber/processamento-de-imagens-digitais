import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lena_gray.jpg",0)
c=255/np.log(1+np.max(img))

log_img=c*np.log(1+img)
log_img=np.array(log_img,dtype=np.uint8)
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.figure()

plt.imshow(log_img,cmap='gray')
plt.axis('off')

plt.show()

