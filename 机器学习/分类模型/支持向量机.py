import numpy as np
import sklearn.preprocessing as sp
import sklearn.utils as su
import sklearn.model_selection as ms
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import sklearn.svm as svm

data = np.loadtxt('../data/multiple2.txt', delimiter=',', unpack=False, dtype='f8')
x = data[:, :2]
y = data[:, -1]
print(x.shape, y.shape)

# 拆分测试集与训练集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, random_state=7)

# 创建SVM分类器
# model = svm.SVC(kernel='linear') #线性核函数
# model = svm.SVC(kernel='poly', degree=3)  #多项式核函数
model = svm.SVC(kernel='rbf', C=600, gamma=0.01) #径向基核函数

model.fit(train_x, train_y)
# 使用测试集测试
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

# 绘制每个样本
mp.figure('SVM Classification', facecolor='lightgray')
mp.title('SVM Classification', fontsize=14)

# 绘制分类边界线
n = 500
l, r = test_x[:, 0].min() - 1, test_x[:, 0].max() + 1
b, t = test_x[:, 1].min() - 1, test_x[:, 1].max() + 1
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))

mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(mesh_x)
grid_z = grid_z.reshape(grid_x.shape)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray', shading='auto')

mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg_r', s=80, label='Simples')

mp.legend()
mp.show()
