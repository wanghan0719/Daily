import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import sklearn.pipeline as pl
import sklearn.preprocessing as sp

x, y = np.loadtxt('../data/single.txt', delimiter=',', unpack=True)
# x = x.reshape(50, 1)
x = x.reshape(-1, 1)  # 自适应转换
# 训练多项式回归模型
model = pl.make_pipeline(sp.PolynomialFeatures(10), lm.LinearRegression())
model.fit(x, y)
pred_y = model.predict(x)
np.sort(x)

# 绘制样本
mp.figure('Polynomial Regression', facecolor='lightgray')
mp.title('Polynomial Regression', fontsize=16)
mp.grid(linestyle=':')
mp.scatter(x, y, color='dodgerblue', label='Samples', s=80)

# 绘制回归线(样本的数据无序，画图须先排序)
px = np.linspace(x.min(), x.max(), 200)
px = px.reshape(-1, 1)
py = model.predict(px)
mp.plot(px, py, color='pink', label='Polynomial line')

mp.legend()
mp.show()

"""
评估训练结果误差
"""
# 平均绝对值误差：1/m∑|实际输出-预测输出|
print(sm.mean_absolute_error(y, pred_y))
# 平均平方误差：SQRT(1/mΣ(实际输出-预测输 出)^2)
print(sm.mean_squared_error(y, pred_y))
# 中位绝对值误差：MEDIAN(|实际输出-预测输出|)
print(sm.median_absolute_error(y, pred_y))
# R2得分，(0,1]区间的分值。分数越高，误差越小。
print(sm.r2_score(y, pred_y))
