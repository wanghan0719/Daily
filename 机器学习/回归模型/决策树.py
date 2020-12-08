import sklearn.tree as st
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.metrics as sm

boston = sd.load_boston()
print(dir(boston))
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)

x, y, header = boston.data, boston.target, boston.feature_names
# 打乱数据集，拆分训练集和测试集
x, y = su.shuffle(boston.data,boston.target, random_state=7)
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]

# 训练决策模型
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)

# 输出测试结果
pred_test_y = model.predict(test_x)

# 评估模型
score = sm.r2_score(test_y, pred_test_y)
print(score)
print(sm.mean_absolute_error(test_y, pred_test_y))