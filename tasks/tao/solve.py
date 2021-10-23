import cv2, time

img = cv2.imread("kojima.png").astype("uint32")
H = img.shape[0]
W = img.shape[1]
img = img.reshape(W*H, 3)

for p in img:
    time.sleep(0.0001)
    print(chr(p[1]), end="", flush=True)
print()