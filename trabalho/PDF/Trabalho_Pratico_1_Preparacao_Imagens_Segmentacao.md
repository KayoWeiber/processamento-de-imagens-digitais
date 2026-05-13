# TRABALHO PRÁTICO 1

**Disciplina:** Processamento de Imagens

## 1. Contexto

Nas últimas aulas foram estudadas técnicas de realce, suavização e detecção de bordas, como equalização de histograma, filtros de média e Gaussiano, Sharpen, Sobel, Prewitt, Laplaciano e Canny. Este trabalho tem como finalidade aplicar essas técnicas em imagens reais ou semirreais, comparando resultados e justificando escolhas técnicas.

## 2. Objetivo

Aplicar técnicas de pré-processamento e detecção de bordas para preparar uma imagem para uma etapa posterior de segmentação, analisando criticamente quais procedimentos melhoram ou prejudicam o resultado.

## 3. Organização

- O trabalho deve ser realizado em grupos de até 3 alunos.
- A entrega deve ser feita em formato PDF.
- O relatório deve ter entre no mínimo 3 páginas.
- O grupo deve entregar também as imagens resultantes geradas durante os testes e os scripts utilizados, todos incorporados ao relatório.

## 4. Imagens sugeridas para análise

Cada grupo deve escolher três das imagens sugeridas pelo professor As imagens fornecidas em anexo foram preparadas para representar problemas diferentes de processamento.

| Imagem sugerida | Desafio visual | O que observar |
|---|---|---|
| 01_bolas_grama.jpg | Objetos circulares sobre fundo texturizado. | A grama gera ruído visual? O Canny consegue separar os contornos das bolas? |
| 02_brinquedo_pelucia.jpg | Objeto com bordas suaves e textura de tecido/pelo. | O Sharpen ajuda ou exagera textura? A suavização apaga contornos? |
| 03_cachorro_jardim.jpg | Animal com pelos e fundo natural complexo. | O pelo gera muitas bordas? Como o blur altera o resultado? |
| 04_praia_cidade.jpg | Cena ampla com água, areia, pessoas e prédios. | Quais regiões produzem mais bordas? O horizonte e os prédios ficam evidentes? |
| 05_lago_parque.jpg | Paisagem com vegetação e reflexos. | Reflexos e folhas confundem os operadores de borda? |
| 06_ferramentas_mesa.jpg | Objetos metálicos com sombras e contornos fortes. | Qual operador destaca melhor ferramentas e parafusos? |
| 07_flor_planta.jpg | Objeto colorido com fundo de folhas. | Converter para cinza prejudica a separação? A cor poderia ajudar em aula futura? |
| 08_rua_dia.jpg | Cena urbana com muitos objetos, prédios, carros e perspectiva. | Há excesso de bordas? O Canny fica poluído? |
| 09_cidade_noite.jpg | Imagem escura com pontos de luz e reflexos. | Equalização melhora ou gera ruído? O threshold do Canny precisa ser ajustado? |

## 5. Técnicas que devem ser utilizadas

O grupo deve aplicar obrigatoriamente as técnicas abaixo:

- Conversão para escala de cinza.
- Pelo menos uma técnica de realce ou ajuste: equalização de histograma ou filtro Sharpen.
- Pelo menos uma técnica de suavização: filtro de média ou filtro Gaussiano.
- Pelo menos dois operadores de borda entre: Sobel, Prewitt, Laplaciano e Canny.

O grupo pode aplicar outras técnicas estudadas, desde que explique por que elas foram utilizadas.

## 6. O que o relatório deve conter

**Identificação:** nome dos integrantes, disciplina, título do trabalho e imagem escolhida.

**Imagem original:** apresentar a imagem escolhida e justificar por que ela foi selecionada.

**Processamentos aplicados:** descrever quais técnicas foram aplicadas e em qual ordem.

**Resultados visuais:** apresentar uma figura comparativa com a imagem original e as imagens processadas.

**Análise crítica:** explicar quais técnicas melhoraram, quais pioraram e por quê.

**Conclusão:** indicar qual sequência de processamento foi mais adequada para a imagem analisada.

## 7. Perguntas obrigatórias para orientar a análise

- A imagem original apresenta baixo contraste, ruído, iluminação irregular ou excesso de detalhes?
- A equalização de histograma melhorou a imagem? Em quais regiões?
- A suavização ajudou a reduzir ruído ou apagou detalhes importantes?
- Qual operador de borda produziu o melhor resultado visual?
- Qual operador gerou mais ruído ou falsas bordas?
- O Canny precisou de ajuste nos valores de threshold? O que aconteceu quando os valores foram alterados?
- O resultado final já parece adequado para uma etapa de segmentação? Justifique.

## 8. Critérios de avaliação

| Critério | Pontuação |
|---|---:|
| Relatório organizado e objetivo | 2,0 |
| Aplicação correta das técnicas obrigatórias | 2,0 |
| Comparação visual clara dos resultados | 2,0 |
| Análise crítica dos efeitos das técnicas | 2,0 |
| Conclusão coerente indicando o melhor pipeline | 2,0 |

## 9. Entrega

https://forms.gle/TMsMqBMb14RQUF9c6

- Arquivo em PDF contendo o relatório.
- O PDF deve conter todas as imagens comparativas necessárias para compreender os resultados.
- O código utilizado DEVE ser anexado ao final do relatório, mas não substitui a análise textual.

## 10. Modelo de conclusão esperada

Exemplo de texto final:

Para a imagem analisada, o melhor resultado foi obtido após a aplicação de __________________, seguida de __________________. A técnica __________________ melhorou a visualização porque __________________. O operador de borda __________________ produziu o resultado mais adequado, pois __________________. Antes de uma segmentação completa, ainda seria necessário __________________.

## 11. Observação importante

O objetivo do trabalho não é apenas gerar imagens processadas. O ponto principal é interpretar os resultados. Portanto, o grupo deve justificar tecnicamente as escolhas realizadas e explicar os efeitos observados.
