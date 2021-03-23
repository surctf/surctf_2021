import numpy as np
import cv2

np.random.seed(1337)

img = cv2.imread("src.png")

IMG_W = img.shape[1]
IMG_H = img.shape[0]

enc_img = np.zeros(img.shape, dtype="uint8")

for i in range(IMG_H):
	shuffle_map = np.arange(IMG_W)
	np.random.shuffle(shuffle_map)
	
	for j in range(IMG_W):
		enc_img[i, j] = img[i, shuffle_map[j]]

cv2.imwrite("enc.png", enc_img)
