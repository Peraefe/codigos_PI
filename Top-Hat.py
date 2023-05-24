"""
Universidade Federal do Tocantins - Campus Palmas
Discilina: Processamento de imagemns
Professora: Glenda Botelho
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciêmcias da Computação
"""
# Atividade 7
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
def dilatar(imagem, mascara):
    altura, largura = imagem.shape
    tamanho_mascara = mascara.shape[0]
    preenchimento = tamanho_mascara // 2
    imagem_dilatada = np.zeros_like(imagem)
    
    for i in range(preenchimento, altura - preenchimento):
        for j in range(preenchimento, largura - preenchimento):
            correcao = imagem[i - preenchimento:i + preenchimento + 1, j - preenchimento:j + preenchimento + 1]
            dilation = np.max(correcao[mascara.astype(bool)])
            imagem_dilatada[i, j] = dilation
    
    return imagem_dilatada

def erodir(imagem, mascara):
    altura, largura = imagem.shape
    tamanho_mascara = mascara.shape[0]
    preenchimento = tamanho_mascara // 2
    imagem_corroida = np.zeros_like(imagem)
    
    for i in range(preenchimento, altura - preenchimento):
        for j in range(preenchimento, largura - preenchimento):
            correcao = imagem[i - preenchimento:i + preenchimento + 1, j - preenchimento:j + preenchimento + 1]
            erosao = np.min(correcao[mascara.astype(bool)])
            imagem_corroida[i, j] = erosao
    
    return imagem_corroida

def opening(imagem, mascara):
    corroido = erodir(imagem, mascara)
    aberto = dilatar(corroido, mascara)
    return aberto

def transformacao_top_hat(imagem, tamanho_mascara):
    mascara = np.ones((tamanho_mascara, tamanho_mascara), dtype=np.uint8)
    imagem_aberta = opening(imagem, mascara)
    top_hat_imagem = imagem - imagem_aberta
    return top_hat_imagem

# Carrega a imagem em tons de cinza
imagem_cinza = Image.open('./img/imagem_top_hat.jpg').convert('L')
#imagem_cinza = Image.open('./img/imagem.jpg').convert('L')
# Converte a imagem para um array numpy
array = np.array(imagem_cinza)

# Especifica o tamanho da máscara
tamanho_mascara = 5

# Aplica a transformação Top-Hat na imagem
top_hat_imagem = transformacao_top_hat(array, tamanho_mascara)

# Exibe a imagem original e a imagem transformada
pyplot.subplot(1, 2, 1)
pyplot.imshow(imagem_cinza, cmap='gray')
pyplot.title('Imagem original')

pyplot.subplot(1, 2, 2)
pyplot.imshow(top_hat_imagem, cmap='gray')
pyplot.title('Transformação Top-Hat')

pyplot.show()