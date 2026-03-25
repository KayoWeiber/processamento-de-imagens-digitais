import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

canais = ('red', 'green', 'blue')
plt.subplot(2,2,1)
plt.figure(figsize=(10, 5))
plt.title('Histograma por canal de cor')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.axis('off')

for i, cor in enumerate(canais):
    hist = cv2.calcHist([img_rgb], [i], None, [256], [0, 256])
    plt.plot(hist, color=cor,label=f'canal {cor.capitalize()}')
    plt.xlim([0, 256])

plt.subplot(2,2,2)
plt.title('Imagem Original')
plt.imshow(img_rgb)
plt.axis('off')

plt.legend()
plt.grid(True,linestyle='--', alpha=0.6)
plt.show()