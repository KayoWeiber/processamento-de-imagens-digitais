import cv2
import matplotlib.pyplot as plt

gray = cv2.imread("lena_gray.jpg", cv2.IMREAD_GRAYSCALE)
neg = 255 - gray

plt.imshow(neg, cmap='gray')
plt.show()