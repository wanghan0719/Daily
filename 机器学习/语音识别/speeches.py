import numpy as np
import sklearn.metrics as sm
import scipy.io.wavfile as wf
import python_speech_features as sf
import sklearn.svm as svm
import os
import sklearn.preprocessing as sp


def load_files(directory):
    """
    读取directory目录下的所有文件及文件夹，返回一个文件路径字典；
    {‘apple’:[url1,url2,....],‘banana’:[url1,url2,....],‘kiwi’:[url1,url2,....]}
    :param directory: 目录路径
    :return:
    """
    results = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            dir_name = root.split(os.path.sep)[-1]
            if dir_name not in results:
                results[dir_name] = []
            results[dir_name].append(file_path)
    return results


objects = load_files('../data/speeches/training')
# print(objects)
train_x, train_y = [], []
for label, urls in objects.items():
    for url in urls:
        sample_rate, sigs = wf.read(url)
        mfcc = sf.mfcc(sigs, sample_rate)
        mfcc = mfcc.mean(axis=0)
        train_x.append(mfcc)
        train_y.append(label)
# 为label设置标签编码，将字符串转化为数字
encoder = sp.LabelEncoder()
train_y = encoder.fit_transform(train_y)
train_x = np.array(train_x)

objects = load_files('../data/speeches/testing')
# print(objects)
test_x, test_y = [], []
for label, urls in objects.items():
    for url in urls:
        sample_rate, sigs = wf.read(url)
        mfcc = sf.mfcc(sigs, sample_rate)
        mfcc = mfcc.mean(axis=0)
        test_x.append(mfcc)
        test_y.append(label)
# 为label设置标签编码，将字符串转化为数字
test_y = encoder.transform(test_y)
test_x = np.array(test_x)

# 找个模型训练样本
# model = svm.SVC(kernel='linear', probability=True)
# model = svm.SVC(kernel='poly', degree=3, probability=True)
# model = svm.SVC(kernel='rbf', probability=True)

# import sklearn.linear_model as lm
# model = lm.LogisticRegression()

import sklearn.naive_bayes as nb
model=nb.GaussianNB()

model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

# 置信概率
probs = model.predict_proba(test_x)
for y, py, prob in zip(test_y, pred_test_y, probs.max(axis=1)):
    print(y, py, prob)
