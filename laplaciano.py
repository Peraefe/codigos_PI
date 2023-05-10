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
def normalizar(arr, new_min, new_max):
    # Find the minimum and maximum values of the input array
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    
    # Calculate the scaling factor
    scale_factor = (new_max - new_min) / (arr_max - arr_min)
    
    # Normalize the array
    normalized_arr = (arr - arr_min) * scale_factor + new_min
    
    return normalized_arr


def laplaciano(imagem):
    # Aplicando as quatro máscaras do Filtro Laplaciano
    mascara1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    mascara2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    mascara3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    mascara4 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    altura, largura = imagem.shape
    resultado1 = np.zeros((altura, largura), dtype=np.float32)
    resultado2 = np.zeros((altura, largura), dtype=np.float32)
    resultado3 = np.zeros((altura, largura), dtype=np.float32)
    resultado4 = np.zeros((altura, largura), dtype=np.float32)

    imagem = np.array(imagem, dtype=np.float32)

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            resultado1[i, j] = np.sum(mascara1 * imagem[i-1:i+2, j-1:j+2])
            resultado2[i, j] = np.sum(mascara2 * imagem[i-1:i+2, j-1:j+2])
            resultado3[i, j] = np.sum(mascara3 * imagem[i-1:i+2, j-1:j+2])
            resultado4[i, j] = np.sum(mascara4 * imagem[i-1:i+2, j-1:j+2])

    normalized_array1 = normalizar(resultado1, 0, 255)
    normalized_array2 = normalizar(resultado2, 0, 255)
    normalized_array3 = normalizar(resultado3, 0, 255)
    normalized_array4 = normalizar(resultado4, 0, 255)

    subtrair1 = imagem - normalized_array1
    subtrair2 = imagem - normalized_array2
    subtrair3 = imagem - normalized_array3
    subtrair4 = imagem - normalized_array4

    normalizado1 = normalizar(subtrair1, 0, 255)
    normalizado2 = normalizar(subtrair2, 0, 255)
    normalizado3 = normalizar(subtrair3, 0, 255)
    normalizado4 = normalizar(subtrair4, 0, 255)

    Image.fromarray(normalizado1.astype(np.uint8)).save('./img/imagem_agucada1_laplacian.png')
    Image.fromarray(normalizado2.astype(np.uint8)).save('./img/imagem_agucada2.png')
    Image.fromarray(normalizado3.astype(np.uint8)).save('./img/imagem_agucada3.png')
    Image.fromarray(normalizado4.astype(np.uint8)).save('./img/imagem_agucada4.png')

def sobel(imagem):
    # Criação das máscaras de Sobel
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    altura, largura = imagem.shape
    resultado = np.zeros((altura, largura), dtype=np.float32)
    result = np.zeros((altura, largura), dtype=np.float32)

    imagem = np.array(imagem, dtype=np.float32)

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            result[i, j] = np.sum(sobel_x * imagem[i-1:i+2, j-1:j+2])
    
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            resultado[i, j] = np.sum(sobel_y * result[i-1:i+2, j-1:j+2])

    normalized_array = normalizar(resultado, 0, 255)

    Image.fromarray(normalized_array.astype(np.uint8)).save('./img/imagem_agucada_sobel.png')

op = 8

while(op !=0 ):
    op = int(input("O que deseja fazer?\n1-Laplaciano\n2-Filtro Gradiente usando as máscaras de Sobel\n"))
    if(op == 1):
        # Carregando a imagem em escala de cinza
        img = Image.open('./img/imagem_colorida_laplaciano.jpeg').convert('L')
        img_array = np.array(img)
        laplaciano(img_array)
    elif(op == 2):
        # Leitura da imagem em escala de cinza
        img = Image.open('./img/imagem_colorida_sobel.jpg').convert('L')
        img = np.array(img)
        sobel(img)
    


