import numpy as np
import matplotlib.pyplot as mp
import sklearn.preprocessing as sp

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

w0, w1, losses = [1], [1], []

lrate = 0.01
times = 1000
epoches = []  # 存储迭代次数

for i in range(times):
    epoches.append(i + 1)
    loss = ((w0[-1] + w1[-1] * train_x - train_y) ** 2).sum() / 2
    losses.append(loss)
    # print('{:4}> w0={:.8f}, w1={:.8f}, loss={:.8f}'.format(i + 1, w0, w1, loss))

    # 根据公式，求出w0方向上的偏导数
    d0 = (w0[-1] + w1[-1] * train_x - train_y).sum()
    # 根据公式，求出w1方向上的偏导数
    d1 = (train_x * (w0[-1] + w1[-1] * train_x - train_y)).sum()
    # 根据更新公式，更新两个模型参数
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)
print(w0, w1)

# 线性回归图
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=16)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, s=80, color='dodgerblue', label='Samples')
# 把x带入回归方程，求出预测的y，绘制回归直线
pred_train_y = w0[-1] + w1[-1] * train_x
mp.plot(train_x, pred_train_y, color='orangered', label='Regression Line')
mp.legend()
mp.tight_layout()

# 梯度下降过程的参数变化图
mp.figure('Training Progress', facecolor='lightgray')

mp.subplot(311)
mp.title('Training Progress', fontsize=16)
mp.grid(linestyle=':')
mp.plot(epoches, w0[:-1], color='dodgerblue', label='w0')
mp.legend()
mp.tight_layout()

mp.subplot(312)
mp.grid(linestyle=':')
mp.plot(epoches, w1[:-1], color='green', label='w1')
mp.legend()
mp.tight_layout()

mp.subplot(313)
mp.grid(linestyle=':')
mp.plot(epoches, losses, color='pink', label='losses')
mp.legend()
mp.tight_layout()

# 基于三维曲面绘制梯度下降过程中的每一个点。
import mpl_toolkits.mplot3d as axes3d

grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))

grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += ((grid_w0 + x*grid_w1 - y) ** 2) / 2

mp.figure('Loss Function')
ax = mp.gca(projection='3d')
mp.title('Loss Function', fontsize=20)
ax.set_xlabel('w0', fontsize=14)
ax.set_ylabel('w1', fontsize=14)
ax.set_zlabel('loss', fontsize=14)
ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=10, cstride=10, cmap='jet')
ax.plot(w0[:-1], w1[:-1], losses, 'o-', c='orangered', label='BGD')
mp.legend()
mp.show()

# 以等高线的方式绘制梯度下降的过程。
mp.figure('Batch Gradient Descent', facecolor='lightgray')
mp.title('Batch Gradient Descent', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(grid_w0, grid_w1, grid_loss, 10, cmap='jet')
cntr = mp.contour(grid_w0, grid_w1, grid_loss, 10,
                  colors='black', linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1, fmt='%.2f',
          fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered', label='BGD')
mp.legend()

mp.show()
