import numpy as np

# 矩阵的创建
ary = np.arange(1, 7).reshape(2, 3)
print(ary, type(ary))
# 1.numpy.matrix
m = np.matrix(ary, copy=True)
m[0, 0] = 999
print(m, type(m))
print(ary)

m2 = np.mat(ary)
m2[0, 0] = 999
print(m2, type(m2))
print(ary)

m3 = np.mat('1 2 3 4; 5 6 7 8')
print(m3)

# 矩阵乘法
arr = np.array([[1, 1, 1],
                [2, 2, 2],
                [3, 3, 3]])
print(arr * arr)
n = np.mat(arr)
print(n * n)

# 逆矩阵
e = np.mat("1 2 6; 3 5 7; 4 8 9")
# print(e.I)
# print(e * e.I)
# 非方阵的逆（称为广义逆矩阵）
e = np.mat("1 2 6; 3 5 7")
print(e.I)
print(e * e.I)

# ndarray提供的矩阵API
a = np.array([
    [1, 2, 6],
    [3, 5, 7],
    [4, 8, 9]])
# 点乘法求ndarray的点乘结果，与矩阵的乘法运算结果相同
k = a.dot(a)
print(k)
# linalg模块中的inv方法可以求取a的逆矩阵
l = np.linalg.inv(a)
print(l)

# 解方程
prices = np.mat('3 3.2; 3.5 3.6')
totals = np.mat('118.4; 135.2')

x = np.linalg.lstsq(prices, totals, rcond=-1)[0]  # 求最小二乘解,拟合
print(x)

x = np.linalg.solve(prices, totals)  # 求解线性方程的解
print(x)

x = prices.I * totals  # 利用矩阵的逆进行求解
print(x)

# 案例：斐波那契数列
n = 35


# 使用递归实现斐波那契数列
def fibo(n):
    return 1 if n < 3 else fibo(n - 1) + fibo(n - 2)


print(fibo(n))

# 使用矩阵实现斐波那契数列
print(int((np.mat('1. 1.; 1. 0.') ** (n - 1))[0, 0]))
