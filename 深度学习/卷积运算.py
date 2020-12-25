from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sn
import cv2 as cv

face = cv.imread('lyf.jpg', flags=0)

# flt = np.array([[-1, 0, 1],
#                 [-2, 0, 2],
#                 [-1, 0, 1]])  # 卷积核，水平方向轮廓

flt = np.array([[1, 2, 1],
                [0, 0, 0],
                [-1, -2, -1]])  # 卷积核，垂直方向轮廓

grad = signal.convolve2d(face,  # 原始数据
                         flt,  # 卷积核
                         boundary='symm',  # 边界处理方式symm
                         mode='same').astype('i4')
plt.figure('Conv2d')
plt.subplot(121)
plt.imshow(face, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(grad, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.show()
