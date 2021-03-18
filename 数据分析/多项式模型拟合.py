'''
1. 计算两只股票的差价
2. 利用多项式拟合求出与两只股票差价相近的多项式系数，最高次为4
'''
import numpy as np
import datetime as dt


# 1.读取数据
# 日期格式转换函数: 将日月年转换为年月日格式
def dmy2ymd(dmy):
    dmy = str(dmy, encoding="utf-8")
    # 从指定字符串返回一个日期时间对象
    dat = dt.datetime.strptime(dmy, "%d-%m-%Y").date()  # 字符串转日期
    tm = dat.strftime("%Y-%m-%d")  # 日期转字符串
    return tm


dates, bhp_close_prices = np.loadtxt("data/bhp.csv",  # 文件路径
                                     delimiter=",",  # 指定分隔符
                                     usecols=(1, 6),  # 读取的列(下标从0开始)
                                     unpack=True,  # 拆分数据
                                     dtype="M8[D], f8",  # 指定每一列的类型
                                     converters={1: dmy2ymd})  #
dates, vale_close_prices = np.loadtxt("data/vale.csv",  # 文件路径
                                      delimiter=",",  # 指定分隔符
                                      usecols=(1, 6),  # 读取的列(下标从0开始)
                                      unpack=True,  # 拆分数据
                                      dtype="M8[D], f8",  # 指定每一列的类型
                                      converters={1: dmy2ymd})  #

# 2.绘制图像
import matplotlib.pyplot as mp
import matplotlib.dates as md

# 绘制k线图，x轴为日期
mp.figure("Polyfit", facecolor="lightgray")
mp.title("Polyfit")
mp.xlabel("Date", fontsize=12)
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

# 绘制差价函数
diff_prices = bhp_close_prices - vale_close_prices
mp.plot(dates, diff_prices, label="diff")

# 寻找拟合差价函数
days = dates.astype("M8[D]").astype("int32")
# 做最小二乘多项式拟合
P = np.polyfit(days,  # x
               diff_prices,  # y
               4)  # 维度
poly_prices = np.polyval(P, days)  # 根据求得的系数，重新计算函数值
mp.plot(dates, poly_prices, label="Polyfit line")
mp.gcf().autofmt_xdate()  # 旋转、共享日期显示

mp.grid(linestyle="--")
mp.legend()
mp.show()
np.diff()