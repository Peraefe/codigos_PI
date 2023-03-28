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

def reduzir_vizinho(imagem):
    altura=len(imagem)     # procura o número de linhas
    largura=len(imagem[0])  # procura o número de coluna

    resultado = [[]] # cria uma matriz com uma linha
    # nova_img= Image.new("L", (largura, altura))

    # x=0
    # y=0
    for i in range(0, altura,2):
        for j in range(0,largura,2):
            resultado.append(imagem[i][j])
            # cor=imagem[i][j]
            # print("cor: ",cor,"\n")
            # nova_img.putpixel((x, y), cor)
            # y=y+1
        # x=x+1

    np_array= np.array(resultado)

    nova_img = Image.fromarray(np_array)

    return nova_img

# def main():
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

 # pega a opção que o cliente quer fazer com a imagem
op = int(input("O que deseja fazer com a sua imagem? 1-Ampliar 2-Redizir"))

 # pega o tipo de interpolação que o cliente deseja
op2 = int(input("1-Imterpolação por vizinho mais próximo 2-Interpolação bilinear"))

 # esrutura condicional que define a função para ser executada de acordo com as opções do cliente
if op == 1:
    if op2 == 1:
        # Amplia a imagem original com vizinho + proximo
        img_ampliada = ampliar_vizinho(imagem)
        # Salva a nova imagem ampliada
        img_ampliada.save("./img/imagem_ampliada.png")
    elif op2 == 2:
        # Amplia a imagem original com interpolação bilinear
        img_ampliada = ampliar_bilinear(imagem)
        # Salva a nova imagem reduzida
        img_ampliada.save("./img/imagem_reduzida.png")
elif op == 2:
    if op2 == 1:
        # Reduz a imagem original com vizinho + proximo
        img_reduzida = reduzir_vizinho(imagem)
        # Salva a nova imagem ampliada
        img_reduzida.save("./img/imagem_ampliada.png")
    elif op2 == 2:
        # Reduz a imagem original com interpolação bilinear
        img_reduzida = reduzir_bilinear(imagem)
        # Salva a nova imagem reduzida
        img_reduzida.save("./img/imagem_reduzida.png")



    
    

