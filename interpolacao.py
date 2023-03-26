"""
Universidade Federal do Tocantins - Campus Palmas
Discilina: Processamento de Imagens
Professora: Glenda Botelho
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciêmcias da Computação
"""
# Atividade 1
# Biblioteca numpy está sendo importada
import numpy as np
# Bibliotecas PIL e matplotlib sendo importadas
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
"""
Para baixar as bibliotecas basta colocar o seguinte código no terminal python do VsCode:
pip install numpy
pip install matplotlib
(Com esse comando a biblioteca PIL vai ser instalada no mesmo pacote)
"""
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('./img/imagem_colorida.jpeg')

# converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

# salva a nova imagem
img_escala_de_cinza.save('./img/imagem_tons_cinza.jpeg')

# transforma a imagem em matriz
data = image.imread('./img/imagem_tons_cinza.jpeg')
print("Imagem -> Matriz")

imagem = data

n_linhas = len(imagem)     # procura o número de linhas 
n_colunas = len(imagem[0])  # procura o número de coluna
matriz = [[]] # cria uma matriz com uma linha
for i in range(0, n_linhas):
    linha = []
    for j in range(0, n_colunas):
        if(i == j):
            print("Entrou aquii 3")
            linha.append(imagem[i][j])
    matriz[i] = linha
img = pyplot.imshow(matriz, aspect='auto')
print("Entrou aquii 4")
print(matriz)
'''pyplot.axis("off")
pyplot.show()'''