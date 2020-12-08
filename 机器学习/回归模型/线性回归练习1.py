import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x, y = np.loadtxt('../data/single.txt', delimiter=',', unpack=True)
# x = x.reshape(50, 1)
x = x.reshape(-1, 1)  # 自适应转换
# 训练线性回归模型
model = lm.LinearRegression()
model.fit(x, y)

# 绘制样本
mp.figure('Liner Regression', facecolor='lightgray')
mp.title('Liner Regression', fontsize=16)
mp.grid(linestyle=':')
mp.scatter(x, y, color='dodgerblue', label='Samples', s=80)
# 绘制回归线
pred_y = model.predict(x)
mp.plot(x, pred_y, color='pink', label='Regression line')
mp.legend()
mp.show()
# 打印模型系数
print(model.intercept_)  # 常量 b
print(model.coef_)  # 系数 [w1,w2,w3,...]

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

"""
模型的保存和加载
"""
import pickle
# 保存模型
# with open('lm.pkl','wb') as f:
#     pickle.dump(model,f)

# 加载模型
with open('lm.pkl','rb') as f:
    model_get= pickle.load(f)
predy=model_get.predict(x)
print(predy)