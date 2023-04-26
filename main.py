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
            if resultado[i][j]<255:
                resultado[i][j]=0
            else:
                resultado[i][j]=255

    nova_img=resultado

    
    return nova_img


def rotular(imagem):
    altura = len(imagem)    # procura por número de linhas
    largura = len(imagem[0])    # procura por número de colunas
    labels = [[0 for j in range(largura)] for i in range(altura)] # cria uma matriz
    equi=[]

    label_count = []
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] == 0: # Pixel preto
                if i==0 and j==0:
                    print("aqui1")
                    labels[i][j]=len(label_count)*1
                    label_count.append(labels[i][j])
                else:
                    if i==0 and imagem[i][j-1]==0:
                        labels[i][j]=imagem[i][j-1]
                    else:
                        if j==0 and imagem[i-1][j]==0:
                            labels[i][j]=labels[i-1][j]
                        else:
                            if j==0 or i==0:
                                labels[i][j]=len(label_count)*1
                                label_count.append(labels[i][j])
                if i > 0 and j>0:
                    if imagem[i-1][j]==255 and imagem[i][j-1]==255:
                            labels[i][j]=len(label_count)*1
                            label_count.append(labels[i][j])
                    elif imagem[i-1][j]==0 and imagem[i][j-1]==0:
                            labels[i][j] = labels[i][j-1]
                            aux=[labels[i-1][j],labels[i][j-1]]
                            equi.append(aux)
                    else:
                        if imagem[i-1][j]==0:
                            labels[i][j]=labels[i-1][j]
                        else:
                            labels[i][j]=labels[i][j-1]
    

    new_equi = []
    for elem in equi:
        if elem not in new_equi:
            if elem[0]!=elem[1]:
                new_equi.append(elem)
    equi = new_equi
    diff=0
    
    while diff!=equi:
        equi = new_equi
        diff=equi 

        for elem in new_equi:
            for i in range(altura):
                for j in range(largura):
                    if labels[i][j]==elem[1]:
                        labels[i][j]=elem[0]
            elem[0]=elem[1]
        
        new_equi = []
        for elem in equi:
            if elem not in new_equi:
                if elem[0]!=elem[1]:
                    new_equi.append(elem)

        for elem in equi:
            for elem2 in equi:
                if elem[0]==elem2[0]:
                    
                if elem[0]==elem2[1]:

    

        diff=new_equi
        print("aqui, equi e diff:",len(equi),len(diff))

    new_count=[]   
    for i in labels:
        for j in i:
            if j not in new_count:
                new_count.append(j)

    print(len(new_count))

    print(label_count)



    np_array= np.array(labels) # transforma o array em um numpy array

    nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

    return nova_img

#def main():
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('atividades\img\imagem_colorida.jpg')
# converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

# salva a nova imagem
img_escala_de_cinza.save('atividades\img\imagem_tons_cinza.jpg')

# transforma a imagem em matriz
data = image.imread('atividades\img\imagem_tons_cinza.jpg')
#data = np.array('./img/imagem_tons_cinza.jpg')
print("Imagem -> Matriz")

imagem = data

#transforma a imagem em binária
imagem=imgbinaria(imagem)

# transforma a imagem em matriz

img_rotulada = rotular(imagem)
img_rotulada.show()
# Salva a nova imagem rotulada
#img_rotulada.save("./img/imagem_rotulada.png")
#np_array= np.array(img_rotulada) # transforma o array em um numpy array
#nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem
#nova_img.show()
#img_rotulada.show()
