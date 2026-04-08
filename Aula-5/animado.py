import cv2
import numpy as np
import matplotlib.pyplot as plt
#Agora vocês estão vendo o kernel andando pela imagem.
#Para cada posição, ele pega uma região 3x3, multiplica pelos pesos do kernel e soma tudo.
#Esse valor calculado substitui o pixel original.
# carregar imagem e reduzir tamanho (IMPORTANTE)
img = cv2.imread("teste2.jpg", 0)
img = cv2.resize(img, (20, 20))  # pequeno para visualização

# kernel média (pode trocar depois)
kernel = np.ones((3,3)) / 9

h, w = img.shape
saida = np.zeros_like(img)

plt.figure(figsize=(10,8))

for i in range(1, h-1):
    for j in range(1, w-1):

        plt.clf()

        # região atual
        regiao = img[i-1:i+2, j-1:j+2]

        # cálculo
        valor = np.sum(regiao * kernel)
        saida[i,j] = valor

        # ---------------- VISUAL ----------------

        # imagem com destaque do pixel atual
        plt.subplot(2,2,1)
        plt.imshow(img, cmap='gray')
        plt.title(f"Posição (i={i}, j={j})")
        plt.scatter(j, i, c='red')
        plt.axis('off')

        # região 3x3
        plt.subplot(2,2,2)
        plt.imshow(regiao, cmap='gray')
        plt.title("Região 3x3")
        plt.axis('off')

        # kernel
        plt.subplot(2,2,3)
        plt.imshow(kernel, cmap='gray')
        plt.title("Kernel")
        plt.axis('off')

        # resultado
        plt.subplot(2,2,4)
        #plt.text(0.1, 0.5, f"Resultado = {valor:.2f}", fontsize=14)
        plt.text(0.1, 0.6, f"Região:\n{regiao}", fontsize=10)
        plt.text(0.1, 0.3, f"Kernel:\n{kernel}", fontsize=10)
        plt.text(0.1, 0.1, f"Soma = {valor:.2f}", fontsize=12)
        plt.axis('off')

        plt.pause(0.2)

plt.show()