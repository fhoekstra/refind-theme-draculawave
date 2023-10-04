# Usage:
# python3 -m venv venv
# source venv/bin/activate
# pip install numpy opencv-python
# python recolor.py path/to/input/png path/to/output/png

import os
import sys
from pathlib import Path

import cv2
import numpy as np

# CONSTANTS

CUSTOM_RGB = (255, 121, 198)
LUT_PATTERN = 'ccw'  # 3 letters out of {'b', 'c', 'w'}, 'bcw' works best for normal pictures, but for fonts I found I had to use 'ccw'
INVERT_COLOR = bool(os.environ.get('INVERT_COLOR')) or False  # If True, inverts the CUSTOM_RGB because something in refind inverts it when we go dark


def main():
    img_path, out_path = parse_args()

    # prepare img
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # extract alpha channel (transparency)
    alpha, img = img[:,:,3], img[:,:,:3]

    result = cv2.LUT(gray(img), get_lut())
    result = np.dstack([result, alpha])

    # save result
    cv2.imwrite(out_path, result)

    cv2.imshow('result', result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


def parse_args():
    # print(f'{sys.argv=}')

    img_path = sys.argv[1]
    if len(sys.argv) > 2:
        out_path = sys.argv[2]
    else:
        out_path = f'out/{img_path}'
        if not (p := Path('out')).is_dir():
            p.mkdir()

    print(f'{img_path=}')
    print(f'{out_path=}')
    print(f'{CUSTOM_RGB=}')

    return img_path, out_path


def gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.merge([gray,gray,gray])


def get_lut():
    def char_to_func(c):
        if c == 'b':
            return black()
        if c == 'w':
            return white()
        return color()
    ls = list(map(char_to_func, LUT_PATTERN))
    lut = np.concatenate(ls, axis=0)
    lut = cv2.resize(lut, (1,256), interpolation=cv2.INTER_CUBIC)
    return lut


def color():
    bgr = CUSTOM_RGB[2], CUSTOM_RGB[1], CUSTOM_RGB[0]
    if INVERT_COLOR:
        bgr = [255-x for x in bgr]  # Invert color because dark theme inverts it
    return np.full((1, 1, 3), bgr, np.uint8)


def black():
    return np.zeros((1, 1, 3), np.uint8)


def white():
    return np.full((1, 1, 3), (255,255,255), np.uint8)



if __name__ == '__main__':
    main()
