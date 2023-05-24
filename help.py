from PIL import Image
import numpy as np

def erodir(imagem, mascara):
    altura, largura = imagem.shape
    tamanho_mascara = mascara.shape[0]
    preenchimento = tamanho_mascara // 2
    imagem_erodida = np.zeros_like(imagem)
    
    for i in range(preenchimento, altura - preenchimento):
        for j in range(preenchimento, largura - preenchimento):
            correcao = imagem[i - preenchimento:i + preenchimento + 1, j - preenchimento:j + preenchimento + 1]
            erosao = np.min(correcao[mascara.astype(bool)])
            imagem_erodida[i, j] = erosao
    
    return imagem_erodida

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


# Carregando a imagem em tons de cinza
img_gray = Image.open('img/imagem_cinza.jpg').convert('L')

# Aplicando uma limiarização para obter uma imagem binária
img_binary = img_gray.point(lambda x: 0 if x < 128 else 255, mode='1')

# Salva
img_binary.save('img/imagem_binaria.png')

# Transforma a imagem em matriz
data = np.array(img_binary)

# Cria máscara de cruz
mascara = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

op = 3

while op != 0:
    op = int(input("O que deseja fazer?\n0-Parar\n1-Erosão\n2-Dilatação\n"))
    if op == 1:
        data = erodir(data,mascara)
        img_result = Image.fromarray(data)
        img_result.show()
    if op == 2:
        data = dilatar(data,mascara)
        img_result = Image.fromarray(data)
        img_result.show()

