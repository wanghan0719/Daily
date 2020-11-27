import numpy as np

"""
数组处理函数
"""
ary = np.arange(1, 8)
print(ary)
# 将调用数组中小于和大于下限和上限的元素替换为下限和上限，返回裁剪后的数组，调用数组保持不变。
ary1 = np.clip(ary, 3, 6)
print(ary1)
# 返回由调用数组中满足条件的元素组成的新数组。  类似掩码的作用
ary2 = np.compress(ary > 3, ary)
print(ary2)
# 返回数组的符号数组
ary = np.append(ary, [0, -1, -3])
ary3 = np.sign(ary)
print(ary3)
"""
加法与乘法通用函数
"""
a = np.arange(1, 7)
print("a:\n", a)  # [1 2 3 4 5 6]
b = np.add(a, a)  # 两数组相加
print("add(a,a):\n", b)  # [ 2  4  6  8 10 12]
c = np.add.reduce(a)  # a数组元素累加和，返回一个值
print("add.reduce(a):\n", c)  # 21
d = np.add.accumulate(a)  # 每个元素和前面元素相加的到新的数组  # 累加和过程
print("add.accumulate(a):\n", d)  # [ 1  3  6 10 15 21]
f = np.add.outer([10, 20, 30], a)  # 外和
print("add.outer(arr, a):\n", f)
g = np.outer([10, 20, 30], a)  # 外积
print("outer(arr, a):\n", g)
h = np.cumprod(a)  # 返回数组中所有元素执行累乘的过程数组
print('cumpord(a):\n', h)
i = np.prod(a)
print('pord(a):\n', i)
"""
除法与取整通用函数
"""

a = np.array([10, 20, -30])
b = np.array([3, -3, 6])
print(np.divide(a, b)) 	# a 真除 b

print(np.floor(a / b))		# （真除的结果向下取整）
print(np.ceil(a / b) )		# （真除的结果向上取整）
print(np.trunc(a / b))		# （真除的结果截断取整）
print(np.round(a / b))		# （真除的结果四舍五入取整）

"""
位运算通用函数
"""
a = np.array([0, -1, 2, -3, 4, -5])
b = np.array([0, 1, 2, 3, 4, 5])
print(a, b)
c = a ^ b
print(c)
# c = a.__xor__(b)
# c = np.bitwise_xor(a, b)
print(np.where(c < 0)[0])
d = np.arange(1, 21)
print(d)
e = d & (d - 1)
e = d.__and__(d - 1)
e = np.bitwise_and(d, d - 1)
print(e)