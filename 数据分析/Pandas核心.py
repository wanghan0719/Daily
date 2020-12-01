import pandas as pd
import numpy as np

"""
pandas描述性统计
"""
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

df = pd.DataFrame(d)
# print(df)
# # 测试描述性统计函数
# print(df.sum())
# print(df.sum(1))
# print(df.mean())
# print(df.mean(1))

# Create a Dictionary of series
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

# Create a DataFrame
df = pd.DataFrame(d)
print(df.describe())
print(df.describe(include=['object', 'number']))

"""
排序
"""
# **按行标签排序**
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
unsorted_df = pd.DataFrame(d)
# 按照行标进行排序
sorted_df = unsorted_df.sort_index()
print(sorted_df)
# 控制排序顺序
sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)

# **按列标签排序**
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
unsorted_df = pd.DataFrame(d)
# 按照列标签进行排序
sorted_df = unsorted_df.sort_index(axis=1)
print(sorted_df)

# **按某列值排序**
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
unsorted_df = pd.DataFrame(d)
# 按照年龄进行排序
sorted_df = unsorted_df.sort_values(by='Age')
print(sorted_df)
# 先按Age进行升序排序，然后按Rating降序排序
sorted_df = unsorted_df.sort_values(by=['Age', 'Rating'], ascending=[True, False])
print(sorted_df)

"""
pandas分组
"""
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
                     'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)
print(df)

# 将数据拆分成组
# 按照年份Year字段分组
print(df.groupby('Year'))
# 查看分组结果
print(df.groupby('Year').groups)

grouped = df.groupby('Year')
# 遍历每个分组
for year, group in grouped:
    print(year)
    print(group)
# 获得一个分组细节
print(grouped.get_group(2014))

# 聚合每一年的平均的分
grouped = df.groupby('Year')
print(grouped['Points'].agg(np.mean))
# 聚合每一年的分数之和、平均分、标准差
grouped = df.groupby('Year')
agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print(agg)

"""
pandas数据表关联操作
"""
left = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty', 'Emma',
                     'Marry', 'Allen', 'Jean', 'Rose', 'David', 'Tom', 'Jack', 'Daniel', 'Andrew'],
    'class_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2],
    'gender': ['M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F'],
    'age': [20, 21, 22, 20, 21, 22, 23, 20, 21, 22, 20, 21, 22, 23, 20, 21, 22, 20, 21, 22],
    'score': [98, 74, 67, 38, 65, 29, 32, 34, 85, 64, 52, 38, 26, 89, 68, 46, 32, 78, 79, 87]})
right = pd.DataFrame(
    {'class_id': [1, 2, 3, 5],
     'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
# 合并两个DataFrame
data = pd.merge(left, right)
print(data)
# 合并两个DataFrame (左连接)
rs = pd.merge(left, right, how='left')
print(rs)

# 合并两个DataFrame (左连接)
rs = pd.merge(left, right, on='subject_id', how='right')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left, right, on='subject_id', how='outer')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left, right, on='subject_id', how='inner')
print(rs)

"""
pandas透视表与交叉表
"""
left = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty', 'Emma',
                     'Marry', 'Allen', 'Jean', 'Rose', 'David', 'Tom', 'Jack', 'Daniel', 'Andrew'],
    'class_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2],
    'gender': ['M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F'],
    'age': [20, 21, 22, 20, 21, 22, 23, 20, 21, 22, 20, 21, 22, 23, 20, 21, 22, 20, 21, 22],
    'score': [98, 74, 67, 38, 65, 29, 32, 34, 85, 64, 52, 38, 26, 89, 68, 46, 32, 78, 79, 87]})
right = pd.DataFrame(
    {'class_id': [1, 2, 3, 5],
     'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
# 合并两个DataFrame
data = pd.merge(left, right)
print(data)

# 以class_id与gender做分组汇总数据，默认聚合统计所有列
print(data.pivot_table(index=['class_id', 'gender']))

# 以class_id与gender做分组汇总数据，聚合统计score列
print(data.pivot_table(index=['class_id', 'gender'], values=['score']))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'],
                       columns=['age']))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'],
                       columns=['age'], margins=True))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'],
                       columns=['age'], margins=True, aggfunc='max'))

