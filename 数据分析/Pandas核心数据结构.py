import pandas as pd
import numpy as np

"""
Series
Series可以理解为一个一维的数组，只是index名称可以自己改动。类似于定长的有序字典，有Index和 value。
"""
# 创建一个空的系列
s = pd.Series()
print(s, type(s))
# 通过一维数组创建Series对象
ary = np.array(['zs', 'ls', 'ww', 'zl', 'tq', 'wb'])
s = pd.Series(ary)
print(s, s[3])
s = pd.Series(ary, index=['001', '002', '003', '004', '005', '006'])
print(s, s['004'], s[3])
# 从字典的方式创建Series对象
data = {'001': 'zs', '002': 'ls', '003': 'wwc', '004': 'qtx', }
s = pd.Series(data)
print(s)
# 通过标量创建Series对象
s = pd.Series(range(3), index=['001', '002', '003'])
print(s)
# 访问Series对象中的数组
ary = np.array(['zs', 'ls', 'ww', 'zl', 'tq', 'wb'])
s = pd.Series(ary)
print(s[[2, 4, 5]])  # 类似索引掩码
print('-' * 100)
# 日期处理
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01',
                   '2011/05/01 01:01:01', '01 Jun 2011', '2011.1.6'])
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
# 获取日期中某个字段的数据
print(dates.dt.month)
# 日期运算
delta = dates - pd.to_datetime('1970-1-1')
print(delta)
print(delta.dt.days)  # 转换为整数int
print('-' * 100)
"""
DateTimeIndex 日期索引
通过指定周期和频率，使用`date.range()`函数就可以创建日期序列。 默认情况下，范围的频率是天。
"""
# 以日为频率
date_list = pd.date_range('2019-08-21', periods=5)
print(date_list)
# 以月为频率
date_list = pd.date_range('2019-08-21', periods=5, freq='M')
print(date_list)
# 生成工作日
date_list = pd.date_range('2019-08-21', periods=5, freq='B')
print(date_list)
# 构建某个区间的时间序列
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
date_list = pd.date_range(start, end)
print(date_list)
# bdate_range()`用来表示商业日期范围
datelist = pd.bdate_range('2011/11/03', periods=5)
print(datelist)
print('-' * 100)

"""
DataFrame
DataFrame是一个类似于表格的数据类型，可以理解为一个二维数组，索引有两个维度，可更改。DataFrame具有以下特点：

- 潜在的列是不同的类型
- 大小可变
- 标记轴(行和列)
- 可以对行和列执行算术运算
"""
# 创建一个空的DataFrame
df = pd.DataFrame()
print(df)
# 从列表创建DataFrame
df = pd.DataFrame([1, 2, 3, 4, 5])
print(df)
data = [['Tom', 12], ['Jerry', 11], ['Lucy', 13]]
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data, index=['001', '002', '003'], columns=['Name', 'Age'])
print(df)
# 数据不够，自动添加NaN
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
# 从字典来创建DataFrame
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
print(df)
data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)

"""
核心数据结构操作
"""