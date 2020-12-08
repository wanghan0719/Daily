import numpy as np
import sklearn.preprocessing as sp
import cv2 as cv
import matplotlib.pyplot as mp

# 均值移除(标准化),**均值移除**可以让样本矩阵中的每一列的平均值为0，标准差为1。
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
r = sp.scale(raw_samples)
print(r)
print(r.mean(axis=0))
print(r.std(axis=0))
print('-' * 100)

# 范围缩放
# 将样本矩阵中的每一列的最小值和最大值设定为相同的区间，统一各列特征值的范围。一般情况下会把特征值缩放至[0, 1]区间
mms = sp.MinMaxScaler(feature_range=(0, 1))
r = mms.fit_transform(raw_samples)
print(r)

# 手动范围缩放
# 1）基本数学计算
# min1=np.min(raw_samples,axis=0)
# print(min1)
# k=raw_samples-min1
# k/=np.max(k,axis=0)
# print(k)
# 2）通过线性方程组
new_ary = []
for i in range(raw_samples.shape[1]):
    col_val = raw_samples[:, i]
    col_min_val = col_val.min()
    col_max_val = col_val.max()
    A = np.array([[col_min_val, 1],
                  [col_max_val, 1]])
    B = np.array([0, 1])
    x = np.linalg.lstsq(A, B, rcond=1)[0]
    new_ary.append(x[0] * col_val + x[1])
new_ary = np.array(new_ary).T
print(new_ary)
print('-' * 100)

"""
归一化
归一化即是用每个样本的每个特征值除以该样本各个特征值绝对值的总和。变换后的样本矩阵，每个样本的特征值绝对值之和为1。
#    l1 - l1范数，向量中个元素绝对值之和
#    l2 - l2范数，向量中个元素平方之和
"""
samples = np.array([[20, 10, 5],
                    [10, 5, 2],
                    [13, 14, 8]])
r = sp.normalize(samples, norm='l1')
print('l1范数计算', r)
print(r.sum(axis=1))
r = sp.normalize(samples, norm='l2')
print('l2范数计算', r)
print((r ** 2).sum(axis=1))
print('-' * 100)

"""
二值化
有些业务并不需要分析矩阵的详细完整数据（比如图像边缘识别只需要分析出图像边缘即可），可以根据一个事先给定的阈值，
用0和1表示特征值不高于或高于阈值。二值化后的数组中每个元素非0即1，达到简化数学模型的目的。
"""
img = cv.imread('data/lyf.jpg', flags=0)
# print(img.shape)
# 对img进行二值化处理
bin = sp.Binarizer(threshold=127)
img2 = bin.transform(img)

mp.subplot(121)
mp.imshow(img, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(122)
mp.imshow(img2, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.show()

"""
### 独热编码
为样本特征的每个值建立一个由一个1和若干个0组成的序列，用该序列对所有的特征值进行编码。
"""
simples = np.mat('1 3 2;7 5 4;1 8 6;7 3 9')
print(simples)
ohe = sp.OneHotEncoder()
r = ohe.fit_transform(simples)
print('独热编码：', r)
print('-' * 100)

""""
### 标签编码
根据字符串形式的特征值在特征序列中的位置，为其指定一个数字标签，用于提供给基于数值算法的学习模型。
标签编码相关API：
"""
raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'ford',
    'audi'])
lbe = sp.LabelEncoder()
r = lbe.fit_transform(raw_samples)
print(r)
# 标签编码逆向转换为字符串
r = lbe.inverse_transform([0, 3, 2, 1])
print(r)

print('-' * 100)
