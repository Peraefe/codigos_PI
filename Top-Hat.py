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
    # Obtém a altura e largura da imagem
    altura, largura = imagem.shape
    # Obtém o tamanho da máscara
    tamanho_mascara = mascara.shape[0]
    # Calcula o preenchimento necessário para percorrer a imagem
    preenchimento = tamanho_mascara // 2
    # Cria uma nova imagem com o mesmo formato da imagem original
    imagem_dilatada = np.zeros_like(imagem)
    
    # Percorre os pixels da imagem, excluindo as bordas
    for i in range(preenchimento, altura - preenchimento):
        for j in range(preenchimento, largura - preenchimento):
            # Obtém a região correspondente à máscara no pixel atual
            correcao = imagem[i - preenchimento:i + preenchimento + 1, j - preenchimento:j + preenchimento + 1]
            # Executa a dilatação aplicando a máscara e obtendo o valor máximo
            dilatacao = np.max(correcao[mascara.astype(bool)])
            # Atribui o valor máximo à posição correspondente na imagem dilatada
            imagem_dilatada[i, j] = dilatacao
    
    return imagem_dilatada

def erodir(imagem, mascara):
    # Obtém a altura e largura da imagem
    altura, largura = imagem.shape
    # Obtém o tamanho da máscara
    tamanho_mascara = mascara.shape[0]
    # Calcula o preenchimento necessário para percorrer a imagem
    preenchimento = tamanho_mascara // 2
    # Cria uma nova imagem com o mesmo formato da imagem original
    imagem_corroida = np.zeros_like(imagem)
    
    # Percorre os pixels da imagem, excluindo as bordas
    for i in range(preenchimento, altura - preenchimento):
        for j in range(preenchimento, largura - preenchimento):
            # Obtém a região correspondente à máscara no pixel atual
            correcao = imagem[i - preenchimento:i + preenchimento + 1, j - preenchimento:j + preenchimento + 1]
            # Executa a erosão aplicando a máscara e obtendo o valor mínimo
            erosao = np.min(correcao[mascara.astype(bool)])
            # Atribui o valor mínimo à posição correspondente na imagem corroida
            imagem_corroida[i, j] = erosao
    
    return imagem_corroida

def abertura(imagem, mascara):
    # Aplica a erosão seguida da dilatação
    erodido = erodir(imagem, mascara)
    dilatado = dilatar(erodido, mascara)
    return dilatado

def transformacao_top_hat(imagem, tamanho_mascara):
    # Cria uma máscara com elementos 1 do tamanho especificado
    mascara = np.ones((tamanho_mascara, tamanho_mascara), dtype=np.uint8)
    # Aplica a operação de abertura na imagem
    imagem_aberta = abertura(imagem, mascara)
    # Realiza a transformação Top-Hat subtraindo a imagem aberta da imagem original
    top_hat_imagem = imagem - imagem_aberta
    return top_hat_imagem

# Carrega a imagem em tons de cinza
#imagem_cinza = Image.open('./img/imagem.jpg').convert('L')
imagem_cinza = Image.open('./img/imagem_top_hat.jpg').convert('L')

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