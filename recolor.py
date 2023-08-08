import sys

import cv2
import numpy as np


print(f'{sys.argv=}')

img_path = sys.argv[1]
if len(sys.argv) == 5:
    custom_rgb = sys.argv[2], sys.argv[3], sys.argv[4]
else:
    custom_rgb = (255, 121, 198)

print(f'{img_path=}')
print(f'{custom_rgb=}')


# prepare img
img = cv2.imread(img_path)
# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.merge([gray,gray,gray])


black = np.zeros((1, 1, 3), np.uint8)
white = np.full((1, 1, 3), (255,255,255), np.uint8)
bgr = custom_rgb[2], custom_rgb[1], custom_rgb[0]
color  = np.full((1, 1, 3), bgr, np.uint8)

lut = np.concatenate((black, color, white), axis=0)

lut = cv2.resize(lut, (1,256), interpolation=cv2.INTER_CUBIC)


result = cv2.LUT(gray, lut)

# save result
cv2.imwrite(f'out/{img_path}', result)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
