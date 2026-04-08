import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar imagem
img = cv2.imread('lena.jpg', 0)

h, w = img.shape

# Kernel Gaussiano 3x3
kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]) / 16

# Criar imagem de saída
saida = np.zeros((h, w))

# Aplicar convolução manual
for i in range(1, h-1):
    for j in range(1, w-1):
        
        # Região 3x3
        regiao = img[i-1:i+2, j-1:j+2]
        
        # Multiplicação elemento a elemento
        valor = np.sum(regiao * kernel)
        
        # Atribuir ao pixel central
        saida[i, j] = valor

# Converter para uint8
saida = saida.astype(np.uint8)

# Mostrar resultado
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Manual Gaussiano")
plt.imshow(saida, cmap='gray')
plt.axis('off')

plt.show()