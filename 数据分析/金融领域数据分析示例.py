"""
移动均线
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
import datetime as dt


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
mp.plot(dates, closing_price, color='dodgerblue', linestyle='-', linewidth=2, label='APPL')

# 5日均线图
# ma5 = np.zeros(closing_price.size - 4)
# for i in range(ma5.size):
#     ma5[i] = np.mean(closing_price[i:i + 5])
# mp.plot(dates[4:], ma5, color='orangered', label='MA-5')

# 卷积函数
"""
卷积函数
a: 数据
b: 卷积核
mode: 卷积类型（full, same, valid）
      full：每个元素参与卷积运算的结果
      same：结果维度等于max(a,b)
      valid：两个数组完全重合部分计算的结果
c = numpy.convolve(a, b, mode="full")
"""
a = np.array([1, 2, 3, 4, 5])
b = np.array([8, 7, 6])

full_conv = np.convolve(a, b, "full")  # 完全卷积
print("full:", full_conv)

same_conv = np.convolve(a, b, "same")  # 同维卷积
print("same:", same_conv)

valid_conv = np.convolve(a, b, "valid")  # 有效卷积
print("valid:", valid_conv)

# 用卷积运算实现5日均线图
ma_conv_5 = np.convolve(closing_price, np.ones(5) / 5, mode='valid')
# mp.plot(dates[4:],  # 从第五天开始绘制
#         ma_conv_5,  # 数据
#         color="orangered",
#         label="MA_5")

# 通过e^x 获取一组期望的卷积核，使用自定义卷积核做卷积运算，实现5日均线
kernel = np.exp(np.linspace(-1, 0, 5))[::-1]
kernel = kernel / kernel.sum()
ma53 = np.convolve(closing_price, kernel, mode='valid')
mp.plot(dates[4:], ma53, color='blue', label='MA-53')

# 10日均线图
ma10 = np.zeros(closing_price.size - 9)
for i in range(ma10.size):
    ma10[i] = np.mean(closing_price[i:i + 10])
# mp.plot(dates[9:], ma10, color='green', label='MA-10')

# 绘制布林带，上轨和下轨线
stds = np.zeros(ma53.size)
for i in range(stds.size):
    stds[i] = np.std(closing_price[i:i + 5])
upper = ma53 + 2 * stds
lower = ma53 - 2 * stds
mp.plot(dates[4:], upper, color='red', label='upper')
mp.plot(dates[4:], lower, color='red', label='lower')
mp.fill_between(dates[4:], upper, lower, upper > lower, color='red', alpha=0.2)
mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()  # 自动格式化当前X轴刻度
mp.show()

# 量化分析建模




