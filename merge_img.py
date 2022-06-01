import os
import cv2
import numpy as np

acc = None

for p in os.listdir():
    if p.endswith('.png'):
        if acc is None:
            acc = cv2.imread(p)
        else:
            acc = np.maximum(acc, cv2.imread(p))

cv2.imwrite('merged.png', acc)
