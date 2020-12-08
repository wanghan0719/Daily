import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x, y = np.loadtxt('../data/abnormal.txt', delimiter=',', unpack=True)
x = x.reshape(-1, 1)  # 自适应转换

# 训练线性回归模型
model = lm.LinearRegression()
model.fit(x, y)

mp.figure('Ridge Regression', facecolor='lightgray')
mp.title('Ridge Regression', fontsize=16)
mp.grid(linestyle=':')

# 绘制样本
mp.scatter(x, y, color='dodgerblue', label='Samples', s=80)

# 基于岭回归创建模型

model_ridge = lm.Ridge(100, fit_intercept=True, max_iter=10000)
model_ridge.fit(x, y)
ridge_pred_y = model_ridge.predict(x)
mp.plot(x, ridge_pred_y, color='dodgerblue', label='Ridge line')

# 基于线性回归模型
pred_y = model.predict(x)
mp.plot(x, pred_y, color='pink', label='Regression line')

mp.legend()
mp.show()

# 打印模型系数
print(model.intercept_)  # 常量 b
print(model.coef_)  # 系数 [w1,w2,w3,...]
