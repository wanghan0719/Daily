import numpy as np

# 基本属性
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.shape)  # 维度
print(a.dtype)  # 元素类型
print(a.ndim)  # 维度 len(shape)
print(a.size)  # 元素数量
print(a.itemsize)  # 元素字节数
print(a.nbytes)  # 总字节数
print(a.real, a.imag, sep='\n')  # 实部 虚部
print(a.T)  # 转置
print([elem for elem in a.flat])  # 扁平迭代器
b = a.tolist()  # 转化为列表list
print(b, type(b))

# 自定义复合类型

data = [
    ('zs', [90, 80, 85], 15),
    ('ls', [92, 81, 83], 16),
    ('ww', [95, 85, 95], 15)
]
# 第一种设置dtype的方式
a = np.array(data, dtype='U3, 3int32, int32')  # U-> Unicode
print(a)
print(a[0]['f0'], ":", a[1]['f1'])
print("=====================================")
# 第二种设置dtype的方式
b = np.array(data, dtype=[('name', 'str_', 2),
                          ('scores', 'int32', 3),
                          ('ages', 'int32', 1)])
print(b[0]['name'], ":", b[0]['scores'])
print("=====================================")

# 第三种设置dtype的方式
c = np.array(data, dtype={'names': ['name', 'scores', 'ages'],
                          'formats': ['U3', '3int32', 'int32']})
print(c[0]['name'], ":", c[0]['scores'], ":", c.itemsize)
print("=====================================")

# 第四种设置dtype的方式
d = np.array(data, dtype={'names': ('U3', 0),
                          'scores': ('3int32', 16),
                          'ages': ('int32', 28)})
print(d[0]['names'], d[0]['scores'], d.itemsize)

print("=====================================")

# 测试日期类型数组
f = np.array(['2011', '2012-01-01', '2013-01-01 01:01:01', '2011-02-01'])
f = f.astype('M8[D]')  # “M8[D]”--> datetime64[D] "D"表示精确到day天(格式必须符合'2013-01-01 01:01:01'，否则转换类型时报错)
f = f.astype('int32')
print(f[3] - f[0])
