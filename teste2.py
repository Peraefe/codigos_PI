import numpy as np
from PIL import Image

def bilinear_interpolation(image, new_size):
    # Obtem a dimensão da imagem original
    height, width = image.shape[0], image.shape[1]
    # Obtem a dimensão da nova imagem
    new_height, new_width = new_size[0], new_size[1]

    # Calcula as proporções de escala para altura e largura
    height_scale = float(height) / new_height
    width_scale = float(width) / new_width

    # Cria uma nova imagem com a dimensão desejada
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Loop por cada pixel da nova imagem
    for i in range(new_height):
        for j in range(new_width):
            # Calcula as coordenadas na imagem original
            x = int(j * width_scale)
            y = int(i * height_scale)

            # Calcula os índices dos pixels vizinhos
            x1 = min(x+1, width-1)
            y1 = min(y+1, height-1)

            # Calcula os pesos para os quatro pixels vizinhos
            weight_x = (x+1 - j*width_scale) / width_scale
            weight_y = (y+1 - i*height_scale) / height_scale
            weight_tl = (1 - weight_x) * (1 - weight_y)
            weight_tr = weight_x * (1 - weight_y)
            weight_bl = (1 - weight_x) * weight_y
            weight_br = weight_x * weight_y

            # Calcula o valor do pixel interpolado
            new_image[i, j] = (
                weight_tl * image[y, x] + 
                weight_tr * image[y, x1] + 
                weight_bl * image[y1, x] + 
                weight_br * image[y1, x1]
            )

    return new_image

# Teste da função com a imagem "lena.png"
image = np.array(Image.open('lena.png'))
new_size = (int(image.shape[0]*0.5), int(image.shape[1]*0.5))
new_image = bilinear_interpolation(image, new_size)
Image.fromarray(new_image).show()
