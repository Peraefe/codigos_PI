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

def rotular(imagem):
    #altura = len(imagem)    # procura por número de linhas
    #largura = len(imagem[0])    # procura por número de colunas
    #labels = [[0 for j in range(largura)] for i in range(altura)] # cria uma matriz
    labels = np.zeros_like(image)
    label_count = 1
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] == 255: # Pixel branco
                if i > 0 and labels[i-1,j]:
                    labels[i,j] = labels[i-1,j]
                elif j > 0 and labels[i,j-1]:
                    labels[i,j] = labels[i,j-1]
                else:
                    labels[i,j] = label_count
                    label_count += 1

    return nova_img

#def main():
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('./img/imagem_colorida.jpg')

# converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

# salva a nova imagem
img_escala_de_cinza.save('./img/imagem_tons_cinza.jpg')

# transforma a imagem em matriz
#data = image.imread('./img/imagem_tons_cinza.jpg')
data = np.array('./img/imagem_tons_cinza.jpg')
print("Imagem -> Matriz")

imagem = data

img_rotulada = rotular(imagem)
# Salva a nova imagem ampliada
#img_rotulada.save("./img/imagem_rotulada.png")
np_array= np.array(img_rotulada) # transforma o array em um numpy array
nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem
nova_img.show()
#img_rotulada.show()
