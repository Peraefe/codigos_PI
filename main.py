"""
Universidade Federal do Tocantins - Campus Palmas
Discilina: Processamento de Imagens
Professora: Glenda Botelho
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciêmcias da Computação
"""
# Atividade 3
# Biblioteca numpy está sendo importada
import numpy as np
# Bibliotecas PIL e matplotlib sendo importadas
from PIL import Image
import matplotlib.image as image
import matplotlib.pyplot as plt
import math
"""
Para baixar as bibliotecas basta colocar o seguinte código no terminal python do VsCode:
pip install numpy
pip install matplotlib
(Com esse comando a biblioteca PIL vai ser instalada no mesmo pacote)
"""

def adicao(imagem1, imagem2):
    # Verifica se as dimensões das imagens são iguais
    if imagem1.size != imagem2.size:
        print("As imagens não têm as mesmas dimensões.")
        exit()

    # Cria uma nova imagem com as mesmas dimensões das duas imagens originais
    imagem_somada = Image.new(imagem1.mode, imagem1.size)

    # Obtém os pixels das duas imagens originais e da nova imagem criada
    pixels1 = imagem1.load()
    pixels2 = imagem2.load()
    pixels_somada = imagem_somada.load()

    # Percorre cada pixel das duas imagens originais, soma os valores dos pixels
    # e armazena o resultado na nova imagem criada
    for i in range(imagem1.size[0]):
        for j in range(imagem1.size[1]):
            pixel1 = pixels1[i, j]
            pixel2 = pixels2[i, j]
            pixel_soma = min(pixel1 + pixel2, 255)
            pixels_somada[i, j] = pixel_soma

    # Exibe a imagem somada
    imagem_somada.show()

def subtracao(imagem1, imagem2):
    # Verifica se as dimensões das imagens são iguais
    if imagem1.size != imagem2.size:
        print("As imagens não têm as mesmas dimensões.")
        exit()

    # Cria uma nova imagem com as mesmas dimensões das duas imagens originais
    imagem_subtraida = Image.new("L", imagem1.size)

    # Obtém os pixels das duas imagens originais e da nova imagem criada
    pixels1 = imagem1.load()
    pixels2 = imagem2.load()
    pixels_subtraida = imagem_subtraida.load()

    # Percorre cada pixel das duas imagens originais, subtrai os valores dos canais de luminosidade
    # e armazena o resultado na nova imagem criada
    for i in range(imagem1.size[0]):
        for j in range(imagem1.size[1]):
            l1 = pixels1[i, j]
            l2 = pixels2[i, j]
            l_sub = max(l1 - l2, 0)
            pixels_subtraida[i, j] = l_sub

    # Exibe a imagem subtraída
    imagem_subtraida.show()

def rotacao(imagem):
    altura = len(imagem)
    largura = len(imagem[0])
    nova_imagem = [[0 for j in range(largura)] for i in range(altura)]
    for i in range(altura):
        for j in range(largura):
            novo_i = j
            novo_j = altura - 1 - i
            if novo_i >= largura or novo_j >= altura:
                continue # ignora pixels que ficam fora da nova imagem
            nova_imagem[novo_j][novo_i] = imagem[i][j]
    return nova_imagem

imagem1 = Image.open("./img/imagem-1_tons_cinza.png").convert('L')
imagem2 = Image.open("./img/imagem-2_tons_cinza.png").convert('L')
data = image.imread('./img/imagem.jpg')
op = 8
while op != 0:
    op = int(input("O que deseja fazer?\n1-Somar\n2-Subtrair\n3-Rotacionar\n0-Sair\n"))
    if(op == 1):
        adicao(imagem1, imagem2)
    elif(op == 2):
        subtracao(imagem1, imagem2)
    elif(op == 3):
        imagem_rotacionada = rotacao(data)
        plt.imshow(imagem_rotacionada, cmap='gray')
        plt.show()