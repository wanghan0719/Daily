import sklearn.tree as st
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.metrics as sm
import numpy as np
import matplotlib.pyplot as mp

boston = sd.load_boston()
print(dir(boston))
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)

x, y, header = boston.data, boston.target, boston.feature_names
# 打乱数据集，拆分训练集和测试集
x, y = su.shuffle(boston.data, boston.target, random_state=7)
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]

# 训练决策模型
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)

# 输出测试结果
pred_test_y = model.predict(test_x)

"""
# 评估模型
"""
score = sm.r2_score(test_y, pred_test_y)
print('决策树模型得分：', score)
print(sm.mean_absolute_error(test_y, pred_test_y))
fi = model.feature_importances_
print(fi, np.argwhere(fi == max(fi)))  # 输出特征重要性,重要性最大的下标

"""
1） 正向激励
# 训练adaboost模型
"""
import sklearn.ensemble as se

model = se.AdaBoostRegressor(model, n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
score = sm.r2_score(test_y, pred_test_y)
print('正向激励决策树模型得分：', score)
fi = model.feature_importances_
print(fi, np.argwhere(fi == max(fi)))

"""
绘制特征重要性
"""
mp.figure('Feature Importance', facecolor='lightgray')
mp.title('Feature Importance', fontsize=16)
mp.grid(linestyle=':', axis='y')
mp.xlabel('Feature', fontsize=14)
mp.ylabel('Importance', fontsize=14)
x = np.arange(fi.size)
# 排序
indices = fi.argsort()[::-1]

mp.bar(x, fi[indices], 0.8, color='dodgerblue', label='Feature Importance')
mp.xticks(x, header[indices])
mp.legend()
mp.tight_layout()
mp.show()

"""
2）自助聚合
3) 随机森林
"""
# 读取样本数据
data = np.loadtxt('../data/bike_day.csv', delimiter=',', dtype='U20')
headers = data[0, 2:13]
x = np.array(data[1:, 2:13], dtype='f8')
y = np.array(data[1:, -1:], dtype='f8').ravel()

# 打乱数据集，拆分测试集与训练集
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]

# 训练随机森林回归模型
model = se.RandomForestRegressor(n_estimators=1000, max_depth=10, min_samples_split=2)
model.fit(train_x, train_y)

# 使用测试集测试模型
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
print(sm.mean_absolute_error(test_y, pred_test_y))

# 基于“天”数据集的特征重要性
fi_dy = model.feature_importances_
print(fi_dy)

# 读取样本数据
data = np.loadtxt('../data/bike_hour.csv', delimiter=',', dtype='U20')
headers = data[0, 2:14]
x = np.array(data[1:, 2:14], dtype='f8')
y = np.array(data[1:, -1:], dtype='f8').ravel()

# 打乱数据集，拆分测试集与训练集
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]

# 训练随机森林回归模型
model = se.RandomForestRegressor(n_estimators=1000, max_depth=10, min_samples_split=2)
model.fit(train_x, train_y)

# 使用测试集测试模型
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
print(sm.mean_absolute_error(test_y, pred_test_y))

# 基于“小时”数据集的特征重要性
fi_hr = model.feature_importances_
print(fi_hr)