import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

"""
逻辑分类
    1）二元分类
"""

# # 逻辑函数
# x = np.linspace(-5, 5, 200)
# y = 1 / (1 + np.exp(-x))
# mp.plot(x,y)
# mp.show()

x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])

# 使用这组样本训练逻辑分类模型
model = lm.LogisticRegression(solver='liblinear', C=1)
model.fit(x, y)
r = model.predict([[3, -1], [5, 16]])
print(r)

# 绘制样本图
mp.figure("Logistic Classification", facecolor='lightgray')
mp.title("Logistic Classification", fontsize=14)

# 绘制分类边界线
n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(mesh_x)
grid_z = grid_z.reshape(grid_x.shape)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray', shading='auto')

# 绘制每个样本
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg_r', s=80, label='Simples')
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)

mp.legend()
mp.show()

"""
逻辑分类：
    2）多元分类：通过构建多个二元分类模型，解决多元分类问题，几元对应几个二元分类模型
        代码除数据之外，与二元分类类似
"""

x = np.array([
    [4, 7],
    [3.5, 8],
    [3.1, 6.2],
    [0.5, 1],
    [1, 2],
    [1.2, 1.9],
    [6, 2],
    [5.7, 1.5],
    [5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])

# 使用这组样本训练逻辑分类模型
model = lm.LogisticRegression(solver='liblinear', C=100)
model.fit(x, y)
r = model.predict([[3, -1], [5, 16]])
print(r)

# 绘制样本图
mp.figure("Logistic Classification", facecolor='lightgray')
mp.title("Logistic Classification", fontsize=14)

# 绘制分类边界线
n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(mesh_x)
grid_z = grid_z.reshape(grid_x.shape)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray', shading='auto')

# 绘制每个样本
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg_r', s=80, label='Simples')
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)

mp.legend()
mp.show()
