# Carregar imagem em escala de cinza
from PIL import Image
import numpy as np

image = Image.open('imagem.jpg').convert('L')
img = np.array(image)

# Definir uma função para rotular cada pixel
def labeling(image):
    labels = np.zeros_like(image)
    label_count = 1
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] == 255: # Pixel branco
                if i > 0 and labels[i-1,j]:
                    labels[i,j] = labels[i-1,j]
                elif j > 0 and labels[i,j-1]:
                    labels[i,j] = labels[i,j-1]
                else:
                    labels[i,j] = label_count
                    label_count += 1
    return labels

# Chamar a função de rotulação e exibir os resultados
labels = labeling(img)
np_array= np.array(labels) # transforma o array em um numpy array
nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem
nova_img.show()
#print(labels)