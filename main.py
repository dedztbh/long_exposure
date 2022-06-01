import cv2
import numpy as np
import sys

vidcap = cv2.VideoCapture(sys.argv[1])

width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = vidcap.get(cv2.CAP_PROP_FPS)
fpm = round(fps * 60)
print('width, height:', width, height)
print('fps, fpm:', fps, fpm)

acc = np.zeros((height, width, 3))
success, im = vidcap.read()
i = 0
while success:
    acc = np.maximum(acc, im)
    div, rem = divmod(i, fpm)
    if rem == 0:
        cv2.imwrite('min{}_fram{}.png'.format(div, i), acc)
        acc = np.zeros((height, width, 3))
    success, _ = vidcap.read(im)
    i += 1

cv2.imwrite('out_img.png', acc)
