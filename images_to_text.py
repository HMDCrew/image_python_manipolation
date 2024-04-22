import cv2
import numpy as np
from skimage.metrics import structural_similarity

from helpers.show_img import show_img, img_helper_dimension, resize

img = cv2.imread("1.tif", cv2.IMREAD_GRAYSCALE)

img_w, img_h = img_helper_dimension(img)
img = resize(cv2, img, img_w, img_h)

# Binarizza l'immagine per separare i punti neri di aggregazione
_, binary_image = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# Trova i contorni nell'immagine binarizzata
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Itera sui contorni trovati
for contour in contours:
    # Calcola il rettangolo del contorno
    x, y, w, h = cv2.boundingRect(contour)
    
    # Disegna il rettangolo rosso intorno al punto nero di aggregazione
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

show_img(cv2, img)

cv2.waitKey(0)
