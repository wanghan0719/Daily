"""
特征值&特征向量
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as mp

A = np.mat('1 3 6; 2 3 8; 4 8 9')
print(A, '<-A')
eigvals, eigvecs = np.linalg.eig(A)
print('特征值：', eigvals)
print('特征向量：', eigvecs)
# 通过特征值特征向量生成矩阵
# 求原方阵 特征向量 * 对角阵 * 逆
B = eigvecs * np.diag(eigvals) * eigvecs.I
print(B, '<-B')

'''
利用特征值与特征向量处理图片
'''
img = cv.imread('data/lyf.jpg', flags=0)
img = np.mat(img)
# print(img.shape)
eigvals, eigvecs = np.linalg.eig(img)
# 抹掉一部分特征值
eigvals[20:] = 0
img2 = eigvecs * np.diag(eigvals) * eigvecs.I

# 对img做奇异值分解，抹掉一部分奇异值，计算原方阵
U, sv, V = np.linalg.svd(img)  # 返回非方阵
# 抹掉一部分奇异值
sv[20:] = 0
img3 = U * np.diag(sv) * V

# 显示原图
mp.subplot(131)
mp.imshow(img, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.subplot(132)
# 显示特征向量分解后，复原后的图
mp.imshow(img2.real, cmap='gray')
mp.xticks([])
mp.yticks([])
# 显示奇异值分解后，复原后的图
mp.subplot(133)
mp.imshow(img3.real, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()

"""
奇异值分解
"""
M = np.mat('4 11 14; 8 7 -2')  # 构建一个非方阵
# print(M)
# 提取奇异值，分解得到三个矩阵
U, sv, V = np.linalg.svd(M,
                         full_matrices=False)  # 返回非方阵
print(U, '<-U')
print(V, '<-V')
print(sv, '<-sv')
# U和V是正交矩阵
print(U * U.T)
print(V * V.T)
# sv[1:] = 0 # 去掉一部分值
S = np.diag(sv)
print(S)
print(U * S * V)


