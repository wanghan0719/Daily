"""
人工分类
# 含分类边界线的制作：pcolormesh方法
"""
import matplotlib.pyplot as mp
import numpy as np

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

# 绘制样本图
mp.figure("Simple Classification", facecolor='lightgray')
mp.title("Simple Classification", fontsize=14)

# 绘制分类边界线
n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
grid_z = np.zeros_like(grid_x)
grid_z[grid_x < grid_y] = 1
grid_z[grid_x > grid_y] = 0
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray', shading='auto')

# 绘制每个样本
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg_r', s=80, label='Simples')
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)

mp.legend()
mp.show()
