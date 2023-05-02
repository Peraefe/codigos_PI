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


def equalizar(imagem):
    altura=len(imagem)     # procura o número de linhas
    largura=len(imagem[0])  # procura o número de coluna

    resultado = [[0 for i in range(altura)] for j in range(largura)] # cria uma matriz
    histograma = [[0 for i in range(255)] for j in range(6)] # cria matriz do histograma

    pixels=altura*largura # numero de pixels da imagem

    
    for i in range(0,altura):
        for j in range(0,largura):
            for k in range(255):
                histograma[0][k]=k # preenche o histograma em Rk inicial
                if (imagem[i][j])==(histograma[0][k]):
                    histograma[1][k]+=1 # preenche o histograma em Nk

    # preenche o histograma em Pr(Nk)
    for k in range(0,255):
        histograma[2][k]=((histograma[1][k])*(1/pixels))
    
        
    for k in range(0,255):
        if k==0:
            histograma[3][k]=histograma[2][k] # preenche o histograma em Freq
            histograma[4][k]=(histograma[3][k])*255 # preenche o histograma em EQ
            histograma[5][k]=round(histograma[4][k]) # preenche o histograma em Rk final
        else:
            histograma[3][k]=(histograma[2][k]+histograma[3][k-1]) # preenche o histograma em Freq
            histograma[4][k]=(histograma[3][k])*255 # preenche o histograma em EQ
            histograma[5][k]=round(histograma[4][k]) # preenche o histograma em Rk final


    for i in range(0,altura):
        for j in range(0,largura):
            for k in range(0,255):
                if imagem[i][j]==histograma[0][k]:
                    resultado[i][j]=histograma[5][k] # usa o histograma para equalizar a imagem e guardar o valor dos pixels em resultado
                
    np_array= np.array(resultado) # transforma o array em um numpy array

    nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

    return nova_img

# def main():
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('atividades\img\imagem_colorida.jpeg')

 # converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

 # salva a nova imagem
img_escala_de_cinza.save('atividades\img\imagem_tons_cinza.jpeg')

 # transforma a imagem em matriz
data = image.imread('atividades\img\imagem_tons_cinza.jpeg')
print("Imagem -> Matriz")

imagem = data

# chama a função de equalização
imagem=equalizar(imagem)

# mostra imagem equalizada
imagem.show()
