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
model = svm.SVC(kernel='rbf', C=600, gamma=0.01, probability=True)  # 径向基核函数

model.fit(train_x, train_y)
# 使用测试集测试
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

"""
置信概率
"""
# 整理测试样本
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
probs = model.predict_proba(prob_x)  # 置信概率矩阵
print(probs)

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

# 绘制测试样本结果
mp.scatter(prob_x[:, 0], prob_x[:, 1], s=80, color='red', marker='D', label='Proba Samples')
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})

mp.legend()
mp.show()

"""
样本类别均衡化
通过类别权重的均衡化，使所占比例较小的样本权重较高，而所占比例较大的样本权重较低，以此平均化不同类别样本对分类模型的贡献，提高模型性能。
class_weight 参数
"""
data = np.loadtxt('../data/imbalance.txt', delimiter=',', unpack=False, dtype='f8')
x = data[:, :2]
y = data[:, -1]
print(x.shape, y.shape)

# 拆分测试集与训练集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, random_state=7)

# 创建SVM分类器
# model = svm.SVC(kernel='linear',class_weight='balanced') #线性核函数
# model = svm.SVC(kernel='poly', degree=3, class_weight='balanced')  # 多项式核函数
# model = svm.SVC(kernel='rbf', C=600, gamma=0.01, class_weight='balanced')  # 径向基核函数

"""
网格搜索，多参数协同调参
"""
# 基于径向基核函数的支持向量机分类器
params = [{'kernel': ['linear'], 'C': [1, 10, 100, 1000]},
          {'kernel': ['poly'], 'C': [1], 'degree': [2, 3]},
          {'kernel': ['rbf'], 'C': [1, 10, 100, 1000], 'gamma': [1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(svm.SVC(probability=True, class_weight='balanced'), params, cv=5)

model.fit(train_x, train_y)
# 使用测试集测试
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

# 绘制每个样本
mp.figure('Class Balance', facecolor='lightgray')
mp.title('Class Balance', fontsize=14)

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
