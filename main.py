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

def find_valley_threshold(image):
    # Obter o histograma da imagem
    histogram = image.histogram()

    # Encontrar o limiar inicial usando o método de Otsu
    _, initial_threshold = image.convert("L").getextrema()

    # Inicializar o limiar ótimo como o limiar inicial
    optimal_threshold = initial_threshold

    # Inicializar a medida de separabilidade mínima como um valor alto
    min_separability = float('inf')

    # Percorrer o histograma para encontrar o limiar ótimo
    for t in range(1, 255):
        # Divide o histograma em dois grupos: pixels abaixo do limiar e pixels acima ou igual ao limiar
        group1 = histogram[:t]
        group2 = histogram[t:]

        # Verificar se algum dos grupos está vazio
        if np.sum(group1) == 0 or np.sum(group2) == 0:
            continue

        # Calcule as probabilidades de cada grupo
        w1 = np.sum(group1) / np.sum(histogram)
        w2 = np.sum(group2) / np.sum(histogram)

        # Calcule as médias de intensidade de cada grupo
        mean1 = np.sum(np.multiply(np.arange(t), group1)) / np.sum(group1)
        mean2 = np.sum(np.multiply(np.arange(t, 256), group2)) / np.sum(group2)

        # Calcule a variância intra-classe de cada grupo
        var1 = np.sum(np.multiply(np.square(np.subtract(np.arange(t), mean1)), group1)) / np.sum(group1)
        var2 = np.sum(np.multiply(np.square(np.subtract(np.arange(t, 256), mean2)), group2)) / np.sum(group2)

        # Calcule a medida de separabilidade entre os grupos
        separability = w1 * w2 * np.square(mean1 - mean2) / (var1 + var2)

        # Atualize o limiar ótimo se a medida de separabilidade for menor que a mínima encontrada até agora
        if separability < min_separability:
            min_separability = separability
            optimal_threshold = t

    return optimal_threshold

# Carregar a imagem
image = Image.open('./img/imagem.jpg')  

# Converter a imagem para escala de cinza
image_gray = image.convert("L")

# Converter a imagem em um array numpy
image_array = np.array(image_gray)

# Encontrar o limiar ótimo usando o método do vale
threshold = find_valley_threshold(image_gray)

# Segmentar a imagem com base no limiar ótimo
image_binary = np.where(image_array > threshold, 255, 0)

# Criar uma imagem PIL a partir do array binário
image_segmented = Image.fromarray(image_binary.astype(np.uint8))

# Exibir a imagem segmentada
pyplot.figure(figsize=(8, 4))
pyplot.subplot(1, 2, 1)
pyplot.imshow(image_gray, cmap='gray')
pyplot.title('Imagem em Escala de Cinza')
pyplot.subplot(1, 2, 2)
pyplot.imshow(image_binary, cmap='gray')
pyplot.title('Imagem Segmentada')
pyplot.show()

