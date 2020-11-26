import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    dat = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    tm = dat.strftime("%Y-%m-%d")  # 格式化
    return tm


dates, opening_price, highest_price, lowest_price, closing_price, volume = np.loadtxt('data/aapl.csv', delimiter=',',
                                                                                      usecols=(1, 3, 4, 5, 6, 7),
                                                                                      unpack=True,
                                                                                      dtype='M8[D],f8,f8,f8,f8,f8',
                                                                                      converters={1: dmy2ymd})
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=17)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Closing Price', fontsize=14)
mp.grid(linestyle=':')
ax = mp.gca()
# 设置主刻度定位器为周定位器(每周一显示文本刻度)
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))  # %b表示月份简写
# 设置次刻度定位器为天定位器
ax.xaxis.set_minor_locator(md.DayLocator())
# 把M8[D]转为md.datetime.datetime类型 matplotlib对于M8[D]类型识别不好
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_price, color='dodgerblue', linestyle='--', linewidth=2, label='APPL')

# 绘制K线图
# 绘制实体
rise = closing_price > opening_price
color = ['white' if x else 'green' for x in rise]  # 列表推导式
# ecolor = ['red' if x else 'green' for x in rise] #列表推导式
ecolor = np.zeros(rise.size, dtype='U5')  # 利用numpy掩码的功能设置边缘色
ecolor[:] = 'green'
ecolor[rise] = 'red'
mp.bar(dates, closing_price - opening_price, width=0.8, bottom=opening_price, color=color, edgecolor=ecolor,
       zorder=3)
# 绘制影线
mp.vlines(dates, lowest_price, highest_price, colors=ecolor)

# 绘制平均线
mean = np.mean(closing_price)
# print(mean)
mp.hlines(mean, dates[0], dates[-1], color="blue", label='mean')

# 加权平均数 成交量加权平均价格 VWAP
vwap = np.average(closing_price, weights=volume)
# print(vwap)
mp.hlines(mean, dates[0], dates[-1], color="pink", label='VWAP')
# 加权平均数 时间加权平均价格 TWAP
times = np.linspace(1, 4, 30)
twap = np.average(closing_price, weights=times)
# print(twap)
mp.hlines(mean, dates[0], dates[-1], color="blue", label='TWAP')

# 最值
max_val = np.max(closing_price)  # 最大值
min_val = np.min(closing_price)  # 最小值
print(min_val, "~", max_val)

min_date = np.argmin(lowest_price)  # 返回最小值的下标/索引
max_date = np.argmax(highest_price)  # 返回最大值的下标/索引
print(dates[min_date], ":", lowest_price[min_date])  # 最低价发生日期及价格
print(dates[max_date], ":", highest_price[max_date])  # 最高价发生日期及价格
# 获取极差
lowest_ptp = np.ptp(lowest_price, )  # 最低价波动范围
highest_ptp = np.ptp(highest_price, )  # 最高价波动范围
print("lowest_ptp:", lowest_ptp)
print("highest_ptp:", highest_ptp)

# 中位数
m = np.median(closing_price)
mp.hlines(m, dates[0], dates[-1], color="violet", label='median')

# 标准差
m = np.mean(closing_price)
dev = closing_price - m  # 偏差
var = np.mean(dev ** 2)  # 总体方差
std = np.sqrt(var)  # 总体标准差
print('标准差：', std)
# numpy提供了std()方法返回标准差
print('标准差：', np.std(closing_price, ddof=1))

# 数组轴向汇总
pass

# 协方差
date, bhp_closing_price = np.loadtxt('data/bhp.csv', delimiter=',', usecols=(1, 6), unpack=True, dtype='M8[D],f8',
                                     converters={1: dmy2ymd})
vale_closing_price = np.loadtxt('data/vale.csv', delimiter=',', usecols=(6,), unpack=True, dtype='f8',
                                converters={1: dmy2ymd})
mp.figure('COV', facecolor='lightgray')
mp.title('COV', fontsize=17)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Closing Price', fontsize=14)
mp.grid(linestyle=':')
ax = mp.gca()
# 设置主刻度定位器为周定位器(每周一显示文本刻度)
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))  # %b表示月份简写
# 设置次刻度定位器为天定位器
ax.xaxis.set_minor_locator(md.DayLocator())
# 把M8[D]转为md.datetime.datetime类型 matplotlib对于M8[D]类型识别不好
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, bhp_closing_price, color='dodgerblue', linewidth=2, label='bhp')
mp.plot(dates, vale_closing_price, color='orangered', linewidth=2, label='vale')
# 统计两组数据的协方差
bhp_mean = np.mean(bhp_closing_price)
vale_mean = np.mean(vale_closing_price)
bhp_dev = bhp_closing_price - bhp_mean
vale_dev = vale_closing_price - vale_mean
cov = np.mean(bhp_dev * vale_dev)
print('协方差：', cov)
coef = cov / (np.std(bhp_closing_price) * np.std(vale_closing_price))
print('相关系数：', coef)
# numpy提供np.corrcoef(a,b)方法，返回相关矩阵
m = np.corrcoef(bhp_closing_price, vale_closing_price)
print('相关系数：', m[0, 1])


