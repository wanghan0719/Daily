import pandas as pd
import numpy as np
import time
import math

data = pd.read_csv('train_E6oV3lV.csv')

# 打印头部信息
print(data.head(5))

# 使用dataframe iterows计算字符数

print('\n\nUsing Iterrows\n\n')
start_time = time.time()
data_1 = data.copy()
n_words = []
for i, row in data_1.iterrows():
    n_words.append(len(row['tweet'].split()))

data_1['n_words'] = n_words
print(data_1[['id', 'n_words']].head())
end_time = time.time()

print('\nTime taken to calculate No. of Words by iterrows :',
      (end_time - start_time), 'seconds')

# 使用Numpy数组计算字符数

print('\n\nUsing Numpy Arrays\n\n')
start_time = time.time()
data_2 = data.copy()
n_words_2 = []

for row in data_2.values:
    n_words_2.append(len(row[2].split()))

data_2['n_words'] = n_words_2
print(data_2[['id', 'n_words']].head())

end_time = time.time()
print('\nTime taken to calculate No. of Words by numpy array : ',
      (end_time - start_time), 'seconds')

# 使用apply方法计算字符数
print('\n\nUsing Apply Method\n\n')
start_time = time.time()
data_3 = data.copy()

data_3['n_words'] = data_3['tweet'].apply(lambda x: len(x.split()))
print(data_3[['id', 'n_words']].head())

end_time = time.time()
print('\nTime taken to calculate No. of Words by Apply Method : ',
      (end_time - start_time), 'seconds')


# 使用向量化方法计算词的个数

def word_count(x):
    return len(x.split())


print('\n\nUsing Function Vectorization\n\n')
start_time = time.time()
data_2 = data.copy()

# 向量化函数
vec_word_count = np.vectorize(word_count)
n_words_2 = vec_word_count(data_2['tweet'])

data_2['n_words'] = n_words_2
print(data_2[['id', 'n_words']].head())

end_time = time.time()
print('\nTime taken to calculate No. of Words by numpy array : ',
      (end_time - start_time), 'seconds')
