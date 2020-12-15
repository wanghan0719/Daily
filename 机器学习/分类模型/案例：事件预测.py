import sklearn.preprocessing as sp
import sklearn.svm as svm
import sklearn.model_selection as ms
import numpy as np
import sklearn.metrics as sm


class DigitEncoder():
    """
    数字编码器
    """

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)


# 读取数据，整理输入集与输出集
data = np.loadtxt('../data/events.txt', unpack=False, delimiter=',', dtype='U10')
data = np.delete(data, 1, axis=1)
train_data, encoders = [], []
for column_index in range(data.shape[1]):
    col_val = data[:, column_index]
    if col_val[0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    train_data.append(encoder.fit_transform(col_val))
    encoders.append(encoder)
train_data = np.array(train_data).T

x, y = train_data[:, :-1], train_data[:, -1]
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, random_state=7)

# 训练模型
model = svm.SVC(kernel='rbf', class_weight='balanced')
model.fit(train_x, train_y)

# 评估模型
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

# 模拟真实数据预测
data = [['Tuesday', '13:30:00', '21', '23'],
        ['Monday', '14:30:00', '21', '25']]
data = np.array(data)
test_data = []
for column_index in range(data.shape[1]):
    col_val = data[:, column_index]
    test_data.append(encoders[column_index].transform(col_val))
test_data = np.array(test_data).T
pred_test_y = model.predict(test_data)
print(encoders[-1].inverse_transform(pred_test_y))
