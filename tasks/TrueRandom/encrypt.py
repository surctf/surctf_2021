import numpy as np
import cv2

def get_true_random_number():
    np.random.seed(np.random.randint(1000000))
    return np.random.randint(10000000)

img = cv2.imread("src.png")

IMG_W = img.shape[1]
IMG_H = img.shape[0]

enc_img = np.zeros(img.shape, dtype="uint8")
np.random.seed(IMG_W * IMG_H * 666)

for i in range(IMG_H):
    np.random.seed(get_true_random_number())
    shuffle_map = np.arange(IMG_W)
    np.random.shuffle(shuffle_map)

    for j in range(IMG_W):
        enc_img[i, j] = img[i, shuffle_map[j]]


cv2.imwrite("enc.png", enc_img)
