import numpy as np
import matplotlib.pyplot as mp

# 二项式分布示例

# binomial: 从二项分布中抽取样本
# n:尝试次数  p:概率
r = np.random.binomial(10, 0.3, 200000)
# print(r)
total = 0
probs = []
for i in range(11):
    n = sum(r == i) / 200000
    # print("i:", n)
    probs.append(n)
    total += n
print(total)
print(probs)

x = np.arange(0, 11)
mp.bar(x, probs, color='orangered', label='binominal')
mp.legend()
mp.show()

# 超几何分布
# 从6个好球、4个坏球中抽取3个球，返回好球的数量（执行10次）
n = np.random.hypergeometric(6, 4, 3, 10)
print(n)
print(n.mean())

# 二项分布
samples = np.random.normal(size=10000)

mp.figure('Normal Distribution', facecolor='lightgray')
mp.title('Normal Distribution', fontsize=20)
mp.xlabel('Sample', fontsize=14)
mp.ylabel('Occurrence', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(axis='y', linestyle=':')
mp.hist(samples, 100, density=True, edgecolor='steelblue', facecolor='deepskyblue', label='Normal')

mp.legend()
mp.show()

# 联合间接排序

names = np.array(["Apple", "Huawei", "Mi", "Oppo", "Vivo"])
prices = np.array([8888, 5888, 2999, 3999, 3999])
volumns = np.array([60, 110, 40, 50, 70])

# 排序：先按价格排序，然后按销量排序
indeces = np.lexsort((volumns, prices))  # 排序后返回索引列表（升序）
print(indeces)
print(names[indeces])
indeces = np.lexsort((-volumns, prices))  # 按销量倒序排列
print(indeces)
print(names[indeces])

# 插入排序
a = np.array([1, 2, 4, 5, 6, 8, 9])
b = np.array([7, 3])

c = np.searchsorted(a, b)  # 返回可插入元素的位置
print("pos:", c)

d = np.insert(a, c, b)  # 向a数组中按照c指定的位置插入b数组中的元素
print(d)

"""
# 插值
"""

import scipy.interpolate as si

# 生成一组散点
min_x = -50
max_x = 50
x = np.linspace(min_x, max_x, 15)
y = np.sinc(x)

mp.scatter(x, y, s=60, color="dodgerblue", marker="o", label="Samples")

# 通过样本点生成插值器函数
linear = si.interp1d(x, y, kind='linear')
linear_x = np.linspace(min_x, max_x, 1000)  # 产生一组新的点
linear_y = linear(linear_x)  # 计算y值
mp.plot(linear_x, linear_y, color="green", label="linear interplt")

# 三次样条插值 （Cubic Spline Interpolation） 获得一条光滑曲线
cubic = si.interp1d(x, y, kind='cubic')
cub_x = np.linspace(min_x, max_x, 1000)
cub_y = cubic(cub_x)
mp.plot(cub_x, cub_y, color="orangered", linestyle=':',
        linewidth=4, label="linear interplt")

mp.legend()
mp.show()

"""
积分
"""
import matplotlib.patches as mc
import scipy.integrate as si


def f(x):
    return 2 * x ** 2 + 3 * x + 4


a, b = -5, 5
x1 = np.linspace(a, b, 1001)
y1 = f(x1)

# 利用quad求积分 给出函数f，积分下限与积分上限[a, b]   返回(积分值，最大误差)
area = si.quad(f, a, b)[0]
print("area:", area)

mp.figure('Integral', facecolor='lightgray')
mp.title('Integral', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x1, y1, c='orangered', linewidth=1, label=r'$y=2x^2+3x+4$', zorder=0)
mp.fill_between(x1, y1, 0, y1 >= 0, facecolor='pink')
mp.legend()
mp.show()

"""
图像处理
"""
import cv2 as cv
import scipy.ndimage as sn

# 读取文件
original = cv.imread('data/lyf.jpg', -1)
# 高斯模糊
median = sn.median_filter(original, 21)
# 角度旋转
rotate = sn.rotate(original, 45)
# 边缘识别
prewitt = sn.prewitt(original)
mp.figure('Image', facecolor='lightgray')
mp.subplot(221)
mp.title('Original', fontsize=16)
mp.axis('off')
mp.imshow(original, cmap='gray')
mp.subplot(222)
mp.title('Median', fontsize=16)
mp.axis('off')
mp.imshow(median, cmap='gray')
mp.subplot(223)
mp.title('Rotate', fontsize=16)
mp.axis('off')
mp.imshow(rotate, cmap='gray')
mp.subplot(224)
mp.title('Prewitt', fontsize=16)
mp.axis('off')
mp.imshow(prewitt, cmap='gray')
mp.tight_layout()
mp.show()


"""
金融相关
"""
# 计算终值
# 终值 = np.fv(利率, 期数, 每期支付, 现值)
# 返回期限结束时的值
# 将1000元以1%的年利率存入银行5年，每年加存100元，
# 到期后本息合计多少钱？
fv = np.fv(0.01,  # 利率
           5,  # 福利期数
           -100,  # 支付金额
           -1000)  # 现值
print("fv:", round(fv, 2))

# 计算现值
# 现值 = np.pv(利率, 期数, 每期支付, 终值)
# 将多少钱以1%的年利率存入银行5年，每年加存100元，
# 到期后本息合计fv元？
pv = np.pv(0.01, 5, -100, fv)
print("pv:", pv)

# 净现值 = np.npv(利率, 现金流)
# 将1000元以1%的年利率存入银行5年，每年加存100元，
# 相当于一次性存入多少钱？
npv = np.npv(0.01, [
    -1000, -100, -100, -100, -100, -100])
print("npv:", round(npv, 2))

# 每期支付 = np.pmt(利率, 期数, 现值)
# 以1%的年利率从银行贷款1000元，分5年还清，
# 平均每年还多少钱？
pmt = np.pmt(0.01, 5, 1000)
print("pmt:", round(pmt, 2))

# 期数 = np.nper(利率, 每期支付, 现值)
# 以1%的年利率从银行贷款1000元，平均每年还pmt元，
# 多少年还清？
nper = np.nper(0.01, pmt, 1000)
print("nper:", int(nper))

# 利率 = np.rate(期数, 每期支付, 现值, 终值)
# 从银行贷款1000元，平均每年还pmt元，nper年还清，
# 年利率多少？
rate = np.rate(nper, pmt, 1000, 0)
print("rate:", round(rate, 2))
