import cv2
import numpy as np


def enhance_brightness(image, alpha, beta):
    # Aplica a transformação linear para realçar o contraste
    enhanced_image = np.clip(alpha * image + beta, 0, 255).astype(np.uint8)
    return enhanced_image


imagem = cv2.imread('Normal.jpg')
imagem_21 = cv2.imread('21h.jpg')
imagem_29 = cv2.imread('29h.jpg')
imagem_73 = cv2.imread('73h.jpg')
imagem_96 = cv2.imread('96h.jpg')

contrasted_image = cv2.convertScaleAbs(imagem, alpha=1.2, beta=0)


imagem_cinza_73 = cv2.cvtColor(imagem_73, cv2.COLOR_BGR2GRAY)
imagem_cinza_96 = cv2.cvtColor(imagem_96, cv2.COLOR_BGR2GRAY)
imagem_cinza_29 = cv2.cvtColor(imagem_29, cv2.COLOR_BGR2GRAY)
imagem_cinza_21 = cv2.cvtColor(imagem_21, cv2.COLOR_BGR2GRAY)
imagem_cinzaNormal = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

equalized_image = cv2.equalizeHist(imagem_cinza_29)

equalized_imageNormal = cv2.equalizeHist(imagem_cinzaNormal)


limiar = 200

# Aplicando a transformação para destacar os pontos claros
_, imagem_destacada_96 = cv2.threshold(
    imagem_cinza_96, 220, 255, cv2.THRESH_BINARY)
_, imagem_destacada_73 = cv2.threshold(
    imagem_cinza_73, 175, 255, cv2.THRESH_BINARY)
_, imagem_destacada_29 = cv2.threshold(
    imagem_cinza_29, 210, 255, cv2.THRESH_BINARY)
_, imagem_destacada_21 = cv2.threshold(
    imagem_cinza_21, limiar, 255, cv2.THRESH_BINARY)
_, imagem_destacadaNormal = cv2.threshold(
    imagem_cinzaNormal, 195, 255, cv2.THRESH_BINARY)


# Realce
enhanced_imageNormal = enhance_brightness(imagem, 1.5, 20)
enhanced_image29 = enhance_brightness(imagem_29, 1.5, 20)

# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17))
kernel = np.ones((25, 25), np.uint8)

opening = cv2.morphologyEx(imagem_destacadaNormal, cv2.MORPH_OPEN, kernel)
print(opening == 255)
numero_de_pixels_branco = np.sum(opening == 255)
print(numero_de_pixels_branco)

# Exibindo a imagem original e a imagem com os pontos claros destacados
'''
cv2.namedWindow('Imagem Original 21h', cv2.WINDOW_NORMAL)
cv2.imshow('Imagem Original 21h', imagem_21)
cv2.namedWindow('Pontos Claros Destacados 21h', cv2.WINDOW_NORMAL)
cv2.imshow('Pontos Claros Destacados 21h', imagem_destacada_21)
'''

cv2.namedWindow('Imagem Original normal', cv2.WINDOW_NORMAL)
cv2.imshow('Imagem Original normal', imagem)
cv2.namedWindow('Pontos Claros Destacados normal', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Enhanced Normal', cv2.WINDOW_NORMAL)
cv2.imshow('Pontos Claros Destacados normal', opening)
# cv2.imshow('Enhanced Normal', enhanced_imageNormal)


cv2.waitKey(0)
cv2.destroyAllWindows()