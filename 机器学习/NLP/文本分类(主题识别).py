import numpy as np
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
import sklearn.datasets as sd
import sklearn.model_selection as ms
import sklearn.metrics as sm

train = sd.load_files('../data/20news', encoding='latin1', shuffle=True, random_state=7)
# print(train.data[0])
# print(train.target[0])

# 根据train.data构建tf-idf模型，交给朴素贝叶斯训练
cv = ft.CountVectorizer()
bow = cv.fit_transform(train.data)
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow).toarray()
# 拆分测试集与训练集
train_x, test_x, train_y, test_y = ms.train_test_split(tfidf, train.target, test_size=0.1, random_state=7)
model = nb.MultinomialNB()
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

# 假设有一组样本，预测每个样本的所属类别
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
# 把测试样本转变成与训练样本结构一致的tfidf矩阵
test_bow = cv.transform(test_data)
test_tfidf = tt.transform(test_bow)
pred_test_data = model.predict(test_tfidf)
for sentence, index in zip(test_data, pred_test_data):
    print(sentence, '->', train.target_names[index])
# target_nm=np.array(train.target_names)
# print(target_nm[pred_test_data])
