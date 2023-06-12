"""
Universidade Federal do Tocantins - Campus Palmas
Discilina: Processamento de Imagens
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
import matplotlib.pyplot as plt

def find_valley_threshold(image):
    # Converter a imagem em um array numpy
    image_array = np.array(image)

    # Obter o histograma da imagem
    histogram, bins = np.histogram(image_array.flatten(), bins=256, range=[0, 256])
    #plt.figure(figsize=(10, 5))
    #plt.bar(bins[:-1], histogram, width=1, color='gray')
    #plt.title('Histograma')
    #plt.xlabel('Intensidade')
    #plt.ylabel('Frequência')
    #plt.show()

    # Encontrar o centro do histograma
    center = len(histogram) // 2

    # Inicializar o índice do vale mais próximo ao centro
    closest_valley_index = None

    # Percorrer o histograma para encontrar o vale mais próximo ao centro
    for i in range(center, len(histogram)):
        if histogram[i] < histogram[i-1] and histogram[i] < histogram[i+1]:
            closest_valley_index = i
            break

    if closest_valley_index is None:
        for i in range(center, 0, -1):
            if histogram[i] < histogram[i-1] and histogram[i] < histogram[i+1]:
                closest_valley_index = i
                break

    # Verificar se o vale mais próximo foi encontrado
    if closest_valley_index is not None:
        # Calcular o valor do limiar ótimo como o centro do vale mais próximo
        optimal_threshold = (bins[closest_valley_index] + bins[closest_valley_index+1]) // 2
    else:
        # Caso não seja encontrado um vale, usar o limiar inicial como ótimo
        _, optimal_threshold = image.getextrema()

    #print(optimal_threshold)
    return optimal_threshold

# Carregar a imagem
image = Image.open('img/imagem.jpg')

# Converter a imagem para escala de cinza
image_gray = image.convert("L")

# Encontrar o limiar ótimo usando o método do vale
threshold = find_valley_threshold(image_gray)

# Aplicar o limiar à imagem
image_binary = image_gray.point(lambda pixel: 255 if pixel > threshold else 0, mode='L')

# Exibir a imagem segmentada
pyplot.figure(figsize=(8, 4))
pyplot.subplot(1, 2, 1)
pyplot.imshow(image_gray, cmap='gray')
pyplot.title('Imagem em Escala de Cinza')
pyplot.subplot(1, 2, 2)
pyplot.imshow(image_binary, cmap='gray')
pyplot.title('Imagem Segmentada')
pyplot.show()
