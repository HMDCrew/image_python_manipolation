import cv2
import numpy as np
from skimage.metrics import structural_similarity

from helpers.show_img import show_img, img_helper_dimension, resize

img = cv2.imread("1.tif", cv2.IMREAD_GRAYSCALE)

img_w, img_h = img_helper_dimension(img)
img = resize(cv2, img, img_w, img_h)

def find_black_points(gray_image):

    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Trova i contorni neri
    #contours, _ = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_EXACT)
    #contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Disegna cerchi rossi sui punti neri
    for contour in contours:
        for point in contour:
            cv2.circle(gray_image, (point[0][0], point[0][1]), 3, (0, 0, 255), -1)

    return gray_image

show_img(cv2, find_black_points(img))

cv2.waitKey(0)
