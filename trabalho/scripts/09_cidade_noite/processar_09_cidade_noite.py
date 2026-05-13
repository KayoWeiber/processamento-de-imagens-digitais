from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent
TRABALHO_DIR = BASE_DIR.parents[1]
IMG_PATH = TRABALHO_DIR / "img" / "09_cidade_noite.jpg"
RESULTADOS = BASE_DIR / "resultados"
RESULTADOS.mkdir(parents=True, exist_ok=True)

MPL_CACHE = BASE_DIR.parent / ".matplotlib-cache"
MPL_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE))

import cv2
import matplotlib
import numpy as np


matplotlib.use("Agg")
import matplotlib.pyplot as plt


CANNY_BAIXO = 30
CANNY_ALTO = 100

img_color = cv2.imread(str(IMG_PATH))
if img_color is None:
    raise FileNotFoundError(f"Imagem nao encontrada: {IMG_PATH}")

print("Dimensao da imagem:", img_color.shape)
print(img_color.dtype)
print(img_color[100, 100])

img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
print("Dimensao da imagem em cinza:", img.shape)
print(img[100, 100])

cv2.imwrite(str(RESULTADOS / "00_original.jpg"), img_color)
cv2.imwrite(str(RESULTADOS / "01_original_em_cinza.jpg"), img)

eq = cv2.equalizeHist(img)
cv2.imwrite(str(RESULTADOS / "02_equalizacao_histograma.jpg"), eq)

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.axis("off")
plt.title("imagem original")
plt.imshow(img, cmap="gray")

plt.subplot(2, 2, 2)
plt.title("Histograma Original")
plt.hist(img.ravel(), bins=256)

plt.subplot(2, 2, 3)
plt.axis("off")
plt.title("imagem equalizada")
plt.imshow(eq, cmap="gray")

plt.subplot(2, 2, 4)
plt.title("histograma equalizado")
plt.hist(eq.ravel(), bins=256)
plt.tight_layout()
plt.savefig(RESULTADOS / "histograma_equalizacao.png", dpi=150, bbox_inches="tight")
plt.close()

blur = cv2.blur(img, (3, 3))
cv2.imwrite(str(RESULTADOS / "03_filtro_media.jpg"), blur)

gauss = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite(str(RESULTADOS / "04_filtro_gaussiano.jpg"), gauss)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharp = cv2.filter2D(img, -1, kernel)
cv2.imwrite(str(RESULTADOS / "05_sharpen.jpg"), sharp)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

mag = np.sqrt(sobelx**2 + sobely**2)
mag = cv2.convertScaleAbs(mag)
cv2.imwrite(str(RESULTADOS / "06_sobel_x.jpg"), cv2.convertScaleAbs(sobelx))
cv2.imwrite(str(RESULTADOS / "07_sobel_y.jpg"), cv2.convertScaleAbs(sobely))
cv2.imwrite(str(RESULTADOS / "08_sobel_magnitude.jpg"), mag)

kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

prewidttx = cv2.filter2D(img, cv2.CV_64F, kernelx)
prewidtty = cv2.filter2D(img, cv2.CV_64F, kernely)
prewidttx_abs = cv2.convertScaleAbs(prewidttx)
prewidtty_abs = cv2.convertScaleAbs(prewidtty)
magprewitt = np.sqrt(prewidttx**2 + prewidtty**2)
magprewitt = cv2.convertScaleAbs(magprewitt)
cv2.imwrite(str(RESULTADOS / "09_prewitt_x.jpg"), prewidttx_abs)
cv2.imwrite(str(RESULTADOS / "10_prewitt_y.jpg"), prewidtty_abs)
cv2.imwrite(str(RESULTADOS / "11_prewitt_magnitude.jpg"), magprewitt)

lap = cv2.Laplacian(img, cv2.CV_64F)
lap_abs = cv2.convertScaleAbs(lap)
cv2.imwrite(str(RESULTADOS / "12_laplacian.jpg"), lap_abs)

edges = cv2.Canny(img, CANNY_BAIXO, CANNY_ALTO)
cv2.imwrite(str(RESULTADOS / "13_canny.jpg"), edges)

img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(18, 7))
plt.subplot(2, 5, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(2, 5, 2)
plt.imshow(img, cmap="gray")
plt.title("Escala de cinza")
plt.axis("off")

plt.subplot(2, 5, 3)
plt.imshow(eq, cmap="gray")
plt.title("Equalizacao")
plt.axis("off")

plt.subplot(2, 5, 4)
plt.imshow(blur, cmap="gray")
plt.title("Media")
plt.axis("off")

plt.subplot(2, 5, 5)
plt.imshow(gauss, cmap="gray")
plt.title("Gaussiano")
plt.axis("off")

plt.subplot(2, 5, 6)
plt.imshow(sharp, cmap="gray")
plt.title("Sharpen")
plt.axis("off")

plt.subplot(2, 5, 7)
plt.imshow(mag, cmap="gray")
plt.title("Sobel")
plt.axis("off")

plt.subplot(2, 5, 8)
plt.imshow(magprewitt, cmap="gray")
plt.title("Prewitt")
plt.axis("off")

plt.subplot(2, 5, 9)
plt.imshow(lap_abs, cmap="gray")
plt.title("Laplacian")
plt.axis("off")

plt.subplot(2, 5, 10)
plt.imshow(edges, cmap="gray")
plt.title(f"Canny {CANNY_BAIXO}/{CANNY_ALTO}")
plt.axis("off")

plt.tight_layout()
plt.savefig(RESULTADOS / "comparativo_tecnicas.png", dpi=150, bbox_inches="tight")
plt.close()

print(f"Resultados salvos em: {RESULTADOS}")
