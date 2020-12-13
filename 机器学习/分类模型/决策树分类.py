"""
 小汽车评级
实现一个机器学习模型训练的完整步骤。
   1. 理解需求，整理样本
   2. 分析样本数据特征，离散性，连续性， 选择回归或分类模型。
   3. 数据预处理，标签编码，把每列的标签编码器都存起来。
   4. 训练模型。
   5. 针对测试数据进行测试，测试时使用相同的标签编码器编码数据特征。
   6. 模型评估。
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.utils as su
import sklearn.model_selection as ms
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp

data = np.loadtxt('../data/car.txt', delimiter=',', unpack=False, dtype='U10')

train_data, encoders = [], []
for column_index in range(data.shape[1]):
    column_val = data[:, column_index]
    encoder = sp.LabelEncoder()
    train_data.append(encoder.fit_transform(column_val))
    encoders.append(encoder)
train_data = np.array(train_data).T
train_x = train_data[:, :-1]
train_y = train_data[:, -1]
# 使用空间样本进行训练
model = se.RandomForestClassifier(max_depth=9, n_estimators=140, random_state=7)

"""
验证曲线
验证曲线：模型性能 = f(超参数)
"""
# param_range = np.arange(100, 200, 5)
# train_scores, test_scores = ms.validation_curve(
#     model, train_x, train_y, param_name='n_estimators', param_range=param_range, cv=5)
# f1_scores= test_scores.mean(axis=1)
# mp.figure('validate curve', facecolor='lightgray')
# mp.title('validate curve',fontsize=14)
# mp.xlabel('n_estimators',fontsize=14)
# mp.ylabel('f1_scores',fontsize=14)
# mp.grid(linestyle=':')
# mp.plot(param_range,f1_scores,'o-',color='pink',label='f1 scores')
# mp.legend()
# mp.show()

"""
学习曲线
学习曲线：模型性能 = f(训练集大小)
"""
param_range = np.linspace(0.1, 1, 10)
_, train_scores, test_scores = ms.learning_curve(
    model, train_x, train_y, train_sizes=param_range, cv=5)
f1_scores= test_scores.mean(axis=1)
mp.figure('Learning curve', facecolor='lightgray')
mp.title('Learning curve',fontsize=14)
mp.xlabel('train_sizes',fontsize=14)
mp.ylabel('f1_scores',fontsize=14)
mp.grid(linestyle=':')
mp.plot(param_range,f1_scores,'o-',color='pink',label='train size')
mp.legend()
mp.show()

# 交叉验证
score = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='f1_weighted')
print(score.mean())
model.fit(train_x, train_y)

# 使用model对测试样本进行测试
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]
data = np.array(data)
test_data = []
for column_index in range(data.shape[1]):
    encoder = encoders[column_index]
    test_data.append(encoder.transform(data[:, column_index]))
test_data = np.array(test_data).T
test_x = test_data[:, :-1]
test_y = test_data[:, -1]
pred_test_y = model.predict(test_x)
print(encoders[-1].inverse_transform(pred_test_y))
print(encoders[-1].inverse_transform(test_y))
