import cv2 as cv
import numpy as np

# 读取图片  (b,g,r)
img = cv.imread('../data/lyf.jpg')
print(img.shape)
cv.imshow('img', img)
# 对img进行切片 img[:,:,0],提取蓝色通道
blue = np.zeros_like(img)
blue[:, :, 0] = img[:, :, 0]
# cv.imshow('blue', blue)

# 对img进行切片 img[:,:,1],提取绿色通道
green = np.zeros_like(img)
green[:, :, 1] = img[:, :, 1]
# cv.imshow('green', green)

# 对img进行切片 img[:,:,2],提取红色通道
red = np.zeros_like(img)
red[:, :, 2] = img[:, :, 2]
# cv.imshow('red', red)

# 图像裁剪
h, w = img.shape[:2]
t, b = int(h / 4), int(h * 3 / 4)
l, r = int(w / 4), int(w * 3 / 4)
cropped = img[t:b, l:r, :]
cv.imshow('cropped', cropped)

# 图像缩放 interpolation=线型插值
scaled = cv.resize(cropped, (300, 600))
cv.imshow('scaled', scaled)
scaled2 = cv.resize(cropped, None, fx=2, fy=2)
cv.imshow('scaled2', scaled2)

# 图像保存
# cv.imwrite('red.jpg', red)
cv.waitKey()
