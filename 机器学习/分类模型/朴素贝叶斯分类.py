import numpy as np
import matplotlib.pyplot as mp
import sklearn.naive_bayes as nb
import sklearn.model_selection as ms
import sklearn.metrics as sm

data = np.loadtxt('../data/multiple1.txt', unpack=True, delimiter=',')
data = data.T
x = data[:, :2]
y = data[:, -1]
# print(x.shape, y.shape, data.shape)

# 拆分测试集与训练集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, random_state=7)

# 使用这组样本训练朴素贝叶斯分类模型
model = nb.GaussianNB()

# 先进行交叉验证，看一下这个模型怎么样
# 精准度
score = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='accuracy')
print('精准度：', score)
# 查准率
pw = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='precision_weighted')
print('查准率：', pw)
# 召回率
rw = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='recall_weighted')
print('召回率：', rw)
# f1得分
fw = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='f1_weighted')
print('f1得分：', fw)

model.fit(train_x, train_y)

# 使用测试集测试
pred_test_y = model.predict(test_x)
print('模型预测准确率：', (test_y == pred_test_y).sum() / len(test_y))

# 评估训练结果误差
r2 = sm.r2_score(test_y, pred_test_y)
print('r2得分:', r2)
# 混淆矩阵
# 查准率 = 主对角线上的值 / 该值所在列的和
# 召回率 = 主对角线上的值 / 该值所在行的和
# 行表示实际类别，列表示预测类别。
cm = sm.confusion_matrix(test_y, pred_test_y)
print('混淆矩阵:\n', cm)
# 获取分类报告
cr = sm.classification_report(test_y, pred_test_y)
print('分类报告:\n',cr)

# 绘制样本图
mp.figure("Naive Bayes Classification", facecolor='lightgray')
mp.title("Naive Bayes Classification", fontsize=14)

# 绘制分类边界线
n = 500
l, r = test_x[:, 0].min() - 1, test_x[:, 0].max() + 1
b, t = test_x[:, 1].min() - 1, test_x[:, 1].max() + 1
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))

mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(mesh_x)
grid_z = grid_z.reshape(grid_x.shape)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray', shading='auto')

# 绘制每个样本
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg_r', s=80, label='Simples')
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)

mp.legend()
mp.show()
