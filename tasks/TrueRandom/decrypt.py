import numpy as np
import cv2

np.random.seed(1337)

enc_img = cv2.imread("enc.png")

IMG_W = enc_img.shape[1]
IMG_H = enc_img.shape[0]

dec_img = np.zeros(enc_img.shape, dtype="uint8")

for i in range(IMG_H):
    shuffle_map = np.arange(IMG_W)
    np.random.shuffle(shuffle_map)
    for j in range(IMG_W):
        dec_img[i, shuffle_map[j]] = enc_img[i, j]

cv2.imwrite("dec.png", dec_img)
