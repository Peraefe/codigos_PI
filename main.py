# Bibliotecas necessárias
import numpy as np
from PIL import Image
from matplotlib import image
from matplotlib import pyplot

# Função para transformar uma imagem em tons de cinza em uma imagem binária
def imgbinaria(imagem):
    # Obtém as dimensões da imagem
    altura, largura = imagem.shape
    
    # Cria uma nova matriz para a imagem binária
    resultado = np.zeros((altura, largura), dtype=np.uint8)
    
    # Converte a imagem para binária
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] < 230:
                resultado[i][j] = 0
            else:
                resultado[i][j] = 255
    
    return resultado

# Função para rotular os objetos presentes em uma imagem binária

def rotular(imagem_binaria):
    # Define uma função para encontrar os vizinhos de um pixel dado
    def get_vizinhos(pixel, shape):
        vizinhos = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                x = pixel[0] + i
                y = pixel[1] + j
                if x >= 0 and x < shape[0] and y >= 0 and y < shape[1]:
                    vizinhos.append((x, y))
        return vizinhos
    
    # Cria uma matriz para armazenar os rótulos
    labels = np.zeros(imagem_binaria.shape, dtype=np.uint32)
    
    # Define uma lista de equivalências de rótulos
    equivalencias = []
    
    # Define um rótulo inicial
    proximo_rotulo = 1
    
    # Percorre a imagem binária
    for i in range(imagem_binaria.shape[0]):
        for j in range(imagem_binaria.shape[1]):
            # Se o pixel atual for branco, pula para o próximo
            if imagem_binaria[i,j] == 255:
                continue
            
            # Obtém os vizinhos do pixel atual
            vizinhos = get_vizinhos((i,j), imagem_binaria.shape)
            
            # Cria uma lista de rótulos dos vizinhos conectados
            rotulos_vizinhos = [labels[x,y] for (x,y) in vizinhos if imagem_binaria[x,y] == 0 and labels[x,y] != 0]
            
            # Se nenhum vizinho conectado tiver um rótulo, atribui um novo rótulo
            if not rotulos_vizinhos:
                labels[i,j] = proximo_rotulo
                proximo_rotulo += 15
            
            # Se houver apenas um rótulo entre os vizinhos conectados, atribui esse rótulo
            elif len(rotulos_vizinhos) == 1:
                labels[i,j] = rotulos_vizinhos[0]
            
            # Se houver mais de um rótulo entre os vizinhos conectados, faz a união dos rótulos
            else:
                minimo = min(rotulos_vizinhos)
                maximo = max(rotulos_vizinhos)
                labels[i,j] = minimo
                for e in equivalencias:
                    if maximo in e:
                        e.add(minimo)
                        break
                else:
                    equivalencias.append({minimo, maximo})
    
    # Resolve as equivalências de rótulos
    for e in equivalencias:
        rotulo = min(e)
        for r in e:
            if r != rotulo:
                labels[labels == r] = rotulo
    
    return labels


#def main():
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('atividades\img\imagem_colorida.jpg')
# converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

# salva a nova imagem
img_escala_de_cinza.save('atividades\img\imagem_tons_cinza.jpg')

# transforma a imagem em matriz
data = image.imread('atividades\img\imagem_tons_cinza.jpg')
#data = np.array('./img/imagem_tons_cinza.jpg')
print("Imagem -> Matriz")

imagem = data

#transforma a imagem em binária
imagem=imgbinaria(imagem)
#np_array= np.array(imagem) # transforma o array em um numpy array
#imagem = Image.fromarray(np_array)
#imagem.show()

img_rotulada = rotular(imagem)

np_array= np.array(img_rotulada) # transforma o array em um numpy array

nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

nova_img.show()