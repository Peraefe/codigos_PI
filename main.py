"""
Universidade Federal do Tocantins - Campus Palmas
Discilina: Processamento de Imagens
Professora: Glenda Botelho
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciêmcias da Computação
"""
# Atividade 4
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
# Abre a imagem
imagem = Image.open('img/imagem_colorida.jpg').convert('L')

# Obtém largura e altura da imagem
largura, altura = imagem.size

# Cria uma nova imagem do mesmo tamanho que a original
nova_imagem = Image.new('L', (largura, altura))

# Loop através de cada pixel da imagem original
for x in range(largura):
    for y in range(altura):
        
        # Obtém o valor em tons de cinza do pixel
        cinza = imagem.getpixel((x, y))
        
        # Calcula o novo valor em tons de cinza do pixel
        novo_pixel = 255 - cinza
        
        # Define o novo valor em tons de cinza do pixel na nova imagem
        nova_imagem.putpixel((x, y), novo_pixel)

# Salva a nova imagem em um arquivo
#nova_imagem.save('img/imagem_negativo.jpg')
nova_imagem.show()