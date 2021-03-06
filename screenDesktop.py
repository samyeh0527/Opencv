import numpy as np
import cv2
from mss import mss
from PIL import Image
#定義螢幕左上角與右下角
mon = {'left': 105, 'top': 160, 'width': 1873, 'height': 851}

with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )
        cv2.imshow('test', np.array(img))
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break