from PIL import Image
from PIL import *
from matplotlib import *

def reduzir_imagem(img, taxa_reducao):
    # Calcula as dimensões da nova imagem reduzida
    largura_reduzida = int(img.size[0] * taxa_reducao)
    altura_reduzida = int(img.size[1] * taxa_reducao)

    # Cria uma nova imagem reduzida
    nova_img = Image.new("L", (largura_reduzida, altura_reduzida))

    # Itera sobre os pixels da nova imagem
    for x in range(largura_reduzida):
        for y in range(altura_reduzida):
            # Encontra o pixel correspondente na imagem original mais próximo
            pixel_original_x = round(x / taxa_reducao)
            pixel_original_y = round(y / taxa_reducao)
            pixel_original = img.getpixel((pixel_original_x, pixel_original_y))
            # Copia o valor do pixel correspondente encontrado para a nova imagem reduzida
            nova_img.putpixel((x, y), pixel_original)

    return nova_img

def ampliar_imagem(img, taxa_ampliacao):
    # Calcula as dimensões da nova imagem ampliada
    largura_ampliada = int(img.size[0] * taxa_ampliacao)
    altura_ampliada = int(img.size[1] * taxa_ampliacao)

    # Cria uma nova imagem ampliada
    nova_img = Image.new("L", (largura_ampliada, altura_ampliada))

    # Itera sobre os pixels da nova imagem
    for x in range(largura_ampliada):
        for y in range(altura_ampliada):
            # Encontra o pixel correspondente na imagem original mais próximo
            pixel_original_x = round(x / taxa_ampliacao)
            pixel_original_y = round(y / taxa_ampliacao)
            pixel_original = img.getpixel((pixel_original_x, pixel_original_y))
            # Copia o valor do pixel correspondente encontrado para a nova imagem ampliada
            nova_img.putpixel((x, y), pixel_original)

    return nova_img

# Carrega a imagem original
imagem = Image.open("./img/imagem_colorida.jpeg")

# converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

# salva a nova imagem
img_escala_de_cinza.save('./img/imagem_tons_cinza.jpeg')

img = Image.open("./img/imagem_tons_cinza.jpeg")

# Define a taxa de redução ou ampliação desejada (por exemplo, 50% ou 200%)
taxa_reducao = 0.5
taxa_ampliacao = 2.0

# pega a opção que o cliente quer fazer com a imagem
op = int(input("O que deseja fazer com a sua imagem? 1-Ampliar 2-Redizir"))

# pega o tipo de interpolação que o cliente deseja
op2 = int(input("1-Imterpolação por vizinho mais próximo 2-Interpolação bilinear"))

# esrutura condicional que define a função para ser executada de acordo com as opções do cliente
if op2 == 1:
    if op == 1:
        # Amplia a imagem original
        img_ampliada = ampliar_imagem(img, taxa_ampliacao)
        # Salva a nova imagem ampliada
        img_ampliada.save("./img/imagem_ampliada.png")
    elif op == 2:
        # Reduz a imagem original
        img_reduzida = reduzir_imagem(img, taxa_reducao)
        # Salva a nova imagem reduzida
        img_reduzida.save("./img/imagem_reduzida.png")
elif op2 == 2:
    print("Ainda não foi implementada!")




