# Scripts do Trabalho Pratico 1

Os scripts foram recriados sem base compartilhada. Cada pasta de imagem possui
um arquivo `processar_*.py` independente, com os blocos das aulas copiados para
o proprio script e adaptados apenas para:

- caminho da imagem usada;
- pasta de resultados;
- nome dos arquivos salvos;
- thresholds do Canny.

Mapeamento das aulas usadas:

- `aula-2/aula2-v3.py`: conversao para escala de cinza com `cv2.cvtColor`.
- `aula-4/ex-1.py`: equalizacao com `cv2.equalizeHist`.
- `Aula-5/blur.py`: filtro de media com `cv2.blur`.
- `Aula-5/gauss.py`: filtro Gaussiano com `cv2.GaussianBlur`.
- `Aula-5/sharpen.py`: filtro Sharpen com `cv2.filter2D` e o mesmo kernel.
- `aula-6/ex-2.py`: Sobel X, Sobel Y e magnitude.
- `aula-7/ex-1.py` e `aula-7/ativi-01.py`: Prewitt e Laplaciano.
- `aula-8/ex-1.py`: Canny.

Para gerar tudo:

```bash
python trabalho/scripts/rodar_todos.py
```

