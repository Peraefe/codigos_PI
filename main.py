"""
Universidade Federal do Tocantins - Campus Palmas
Discilina: Processamento de Imagens
Professora: Glenda Botelho
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciêmcias da Computação
"""
# Atividade 5
# Biblioteca numpy está sendo importada
import numpy as np
# Bibliotecas PIL e matplotlib sendo importadas
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import math
"""
Para baixar as bibliotecas basta colocar o seguinte código no terminal python do VsCode:
pip install numpy
pip install matplotlib
(Com esse comando a biblioteca PIL vai ser instalada no mesmo pacote)
"""


def filtro_media(imagem):
    altura=len(imagem)     # procura o número de linhas
    largura=len(imagem[0])  # procura o número de coluna

    zerada= [[0 for i in range(largura)] for j in range(altura)] # cria uma matriz para lidar com borda
    resultado = [[0 for i in range(largura)] for j in range(altura)] # cria uma matriz

    altura-=1
    largura-=1
    for i in range(1,altura):
        for j in range(1,largura):
            zerada[i][j]=imagem[i][j] # usa 0 para valores não calculáveis            

    # aplica o filtro e armazena os resultados na matriz
    for i in range(1,altura-1):
        for j in range(1,largura-1):
            media = ((imagem[i-1][j-1]/9) + (imagem[i-1][j]/9) + (imagem[i-1][j+1]/9) + (imagem[i][j-1]/9) + (imagem[i][j]/9) + (imagem[i][j+1]/9) + (imagem[i+1][j-1]/9) + (imagem[i+1][j]/9) + (imagem[i+1][j+1]/9))
            resultado[i][j] = int(media)
    
    np_array= np.array(resultado) # transforma o array em um numpy array

    nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

    return nova_img

# def main():
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('img\imagem_colorida.jpeg')

# converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

# salva a nova imagem
img_escala_de_cinza.save('img\imagem_tons_cinza.jpeg')

# transforma a imagem em matriz
data = image.imread('img\imagem_tons_cinza.jpeg')
print("Imagem -> Matriz")

imagem = data

# chama a função de filtro
imagem=filtro_media(imagem)

# mostra imagem 
imagem.show()