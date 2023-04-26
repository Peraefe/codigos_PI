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
import math
"""
Para baixar as bibliotecas basta colocar o seguinte código no terminal python do VsCode:
pip install numpy
pip install matplotlib
(Com esse comando a biblioteca PIL vai ser instalada no mesmo pacote)
"""
def imgbinaria(imagem):
    altura = len(imagem)    # procura por número de linhas
    largura = len(imagem[0])    # procura por número de colunas
    resultado = [[0 for i in range(0,altura)] for j in range(0,altura)] # cria uma matriz

    
    for i in range(0, len(resultado)):
        for j in range(0,len(resultado[0])):
            resultado[i][j]=imagem[i][j]

    for i in range(altura):
        for j in range(largura):

            
            if resultado[i][j]<230:
                resultado[i][j]=0
            else:
                resultado[i][j]=255

    nova_img=resultado

    
    return nova_img

def RotulaVizinhanca(imagem,linha, coluna, rotulo):
    altura = len(imagem)    # procura por número de linhas
    largura = len(imagem[0])    # procura por número de colunas

    #Verifica V0
    if coluna!=largura-1:
        if ((coluna+1 <= largura) and (imagem[linha][coluna+1] == 0)):
        
            imagem[linha][coluna+1] = rotulo
            RotulaVizinhanca(imagem, linha, coluna+1, rotulo)
      
   

    #Verifica V1
    if ((imagem[linha-1][coluna] == 0) and (linha-1 >= 0)):
    
        imagem[linha-1][coluna] = rotulo
        RotulaVizinhanca(imagem, linha-1, coluna, rotulo)
      

    #Verifica V2
    if ((imagem[linha][coluna-1] == 0) and (coluna-1 >= 0)):
      
        imagem[linha][coluna-1] = rotulo
        RotulaVizinhanca(imagem, linha, coluna-1, rotulo)
      

    #Verifica V3 
    if linha!=altura-1:
        if ((linha+1 <= altura) and (imagem[linha+1][coluna] == 0)):
        
            imagem[linha+1][coluna] = rotulo
            RotulaVizinhanca(imagem, linha+1, coluna, rotulo)


def rotular(imagem):
    altura = len(imagem)    # procura por número de linhas
    largura = len(imagem[0])    # procura por número de colunas

    rotulo=255

    for i in range(altura):
        for j in range(largura):
            if imagem[i][j]==0:
                imagem[i][j]=rotulo

            RotulaVizinhanca(imagem, i, j, rotulo)

            if (rotulo > 2):
                rotulo-=1
            else:
                print("Sua figura tem mais que 255 componentes conexas!\n");
                break;

    np_array= np.array(imagem) # transforma o array em um numpy array

    nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

    return nova_img



#def main():
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('atividades/img/imagem_colorida.jpg')
# converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

# salva a nova imagem
img_escala_de_cinza.save('atividades/img/imagem_tons_cinza.jpg')

# transforma a imagem em imagem
data = image.imread('atividades/img/imagem_tons_cinza.jpg')
#data = np.array('./img/imagem_tons_cinza.jpg')
print("Imagem -> imagem")

imagem = data

#transforma a imagem em binária
imagem=imgbinaria(imagem)

np_array= np.array(imagem) # transforma o array em um numpy array

nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

nova_img.show()

nova_img.save('atividades\img\imagem_binaria.jpg')

# transforma a imagem em imagem

img_rotulada = rotular(imagem)
#img_rotulada.show()
# Salva a nova imagem rotulada
#img_rotulada.save("./img/imagem_rotulada.png")
#np_array= np.array(img_rotulada) # transforma o array em um numpy array
#nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem
#nova_img.show()
#img_rotulada.show()