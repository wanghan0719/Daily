# 线性拟合示例
import numpy as np
import datetime as dt


#### 1.读取数据
# 日期格式转换函数: 将日月年转换为年月日格式
def dmy2ymd(dmy):
    dmy = str(dmy, encoding="utf-8")
    # 从指定字符串返回一个日期时间对象
    dat = dt.datetime.strptime(dmy, "%d-%m-%Y").date()  # 字符串转日期
    tm = dat.strftime("%Y-%m-%d")  # 日期转字符串
    return tm


dates, open_prices, highest_prices, lowest_prices, close_prices = \
    np.loadtxt('data/aapl.csv',  # 文件路径
               delimiter=",",  # 指定分隔符
               usecols=(1, 3, 4, 5, 6),  # 读取的列(下标从0开始)
               unpack=True,  # 拆分数据
               dtype="M8[D], f8, f8, f8, f8",  # 指定每一列的类型
               converters={1: dmy2ymd})  #

#### 2.绘制图像
import matplotlib.pyplot as mp
import matplotlib.dates as md

# 绘制k线图，x轴为日期
mp.figure("APPL K-Line", facecolor="lightgray")
mp.title("APPL K-Line")
mp.xlabel("Day", fontsize=12)
mp.ylabel("Price", fontsize=12)


# 获取坐标轴
ax = mp.gca()
# 设置主刻度定位器为周定位器(每周一显示刻度文本)
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter("%d %b %Y"))  # %b表示月份简写
# 设置次刻度定位器为天定位器
ax.xaxis.set_minor_locator(md.DayLocator())
mp.tick_params(labelsize=8)
dates = dates.astype(md.datetime.datetime)

# 求得每天的趋势价格: 最高价、最低价、收盘价求平均值作为趋势价
trend_prices = (highest_prices + lowest_prices + close_prices) / 3
mp.scatter(dates, trend_prices, marker="o",
           color="orangered", s=80, label="Trend Points")

# 绘制趋势线
# A：日期转换为数字
# Y: 趋势价格(trend_prices)
days = dates.astype("M8[D]").astype("int32")
# print(days)
# column_stack: 将1d数组堆叠成2d数组
# ones_like: 返回与给定数组具有相同形状和类型的数组
A = np.column_stack((days, np.ones_like(days)))

# lstsq(least-squares solution):最小二乘法，最小化误差的平方和寻找数据的最佳函数匹配
Y = trend_prices
x = np.linalg.lstsq(A, Y, rcond=None)[0]  # x中包含了k, b的值

trend_line = x[0] * days + x[1]  # y = kx + b
mp.plot(dates, trend_line, color="orangered", label="Trend Line")


if x[0] > 0:
    print("总体趋势上涨")
elif x[0] < 0:
    print("总体趋势下跌")
else:
    print("总体趋势持平")

# 顺序放最后，否则会报错
mp.plot(dates, open_prices, color="dodgerblue", linestyle="--")
mp.gcf().autofmt_xdate()  # 旋转、共享日期显示

mp.grid(linestyle="--")
mp.legend()
mp.show()
