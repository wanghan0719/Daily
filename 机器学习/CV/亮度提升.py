import cv2 as cv
import numpy as np

# 亮度提升
img = cv.imread('../data/lyf.jpg')
print(img.shape)
cv.imshow('img', img)

# 将图片转化为灰度图
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# 针对灰度图提亮
e_gray = cv.equalizeHist(gray)
cv.imshow('e_gray', e_gray)

# 彩色图像提亮
# 转换颜色空间 YUV：亮度，色度，饱和度
yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
yuv[:, :, 0] = cv.equalizeHist(yuv[:, :, 0])
color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('color', color)

"""
# Canny边缘识别
    边缘检测常用亮度梯度方法。通过识别亮度梯度变化最大的像素点从而检测出物体的边缘。
"""
canny = cv.Canny(img, 60, 150)
cv.imshow('Canny', canny)

"""
角点检测（针对灰度图处理，降低运算量）
    边缘检测常用亮度梯度方法。通过识别亮度梯度变化最大的像素点从而检测出物体的边缘。
"""
corners = cv.cornerHarris(gray, 7, 5, 0.04)
img[corners > corners.max()*0.01] = [0, 0, 255]
cv.imshow('corners', img)

cv.waitKey()
