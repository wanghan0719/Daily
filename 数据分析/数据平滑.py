import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
import datetime as dt


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    dat = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    tm = dat.strftime("%Y-%m-%d")  # 格式化
    return tm


dates, bhp_closing_price = np.loadtxt('data/bhp.csv', delimiter=',', usecols=(1, 6), unpack=True, dtype='M8[D],f8',
                                      converters={1: dmy2ymd})
vale_closing_price = np.loadtxt('data/vale.csv', delimiter=',', usecols=(6,), unpack=True, dtype='f8',
                                converters={1: dmy2ymd})

mp.figure('BHP&VALE', facecolor='lightgray')
mp.title('BHP&VALE', fontsize=17)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Closing Price', fontsize=14)
ax = mp.gca()
# 设置主刻度定位器为周定位器(每周一显示文本刻度)
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))  # %b表示月份简写
# 设置次刻度定位器为天定位器
ax.xaxis.set_minor_locator(md.DayLocator())
# 把M8[D]转为md.datetime.datetime类型 matplotlib对于M8[D]类型识别不好
dates = dates.astype(md.datetime.datetime)
# mp.plot(dates, bhp_closing_price, color='dodgerblue', linewidth=2, label='bhp')
# mp.plot(dates, vale_closing_price, color='orangered', linewidth=2, label='vale')

# 绘制两只股票收益率曲线
bhp_rate = np.diff(bhp_closing_price) / bhp_closing_price[:-1]
vale_rate = np.diff(vale_closing_price) / vale_closing_price[:-1]
mp.plot(dates[:-1], bhp_rate, color='dodgerblue', label='bhp_rate', alpha=0.2)
mp.plot(dates[:-1], vale_rate, color='orangered', label='vale_rate', alpha=0.2)

# 设置卷积核
# hanning窗: 其中有一个性质, 加hanning窗后，其幅值减为原来的一半
con_kernel = np.hanning(8)
con_kernel /= con_kernel.sum()  # 数据归一化
# 卷积降噪
dates = dates[:-1]
bhp_returns_con = np.convolve(bhp_rate, con_kernel, "valid")  # 卷积运算
vale_returns_con = np.convolve(vale_rate, con_kernel, "valid")  # 卷积运算
mp.plot(dates[7:], bhp_returns_con, color='red', label='bhp_returns_con', alpha=0.3)
mp.plot(dates[7:], vale_returns_con, color='green', label='vale_returns_con', alpha=0.3)

# 针对得到的曲线，做多项式拟合，得到两个多项式方程
days = dates[7:].astype('M8[D]').astype('int32')
bhp_p = np.polyfit(days, bhp_returns_con, 3)
vale_p = np.polyfit(days, vale_returns_con, 3)
bhp_polyval = np.polyval(bhp_p, days)
vale_polyval = np.polyval(vale_p, days)
mp.plot(dates[7:], bhp_polyval, color='red', label='bhp_polyval', linestyle='--')
mp.plot(dates[7:], vale_polyval, color='green', label='vale_polyval', linestyle='--')
# 求两个多项式函数差函数的根，即是两条曲线交点的x坐标
polysub_p = np.polysub(bhp_p, vale_p)
xs = np.roots(polysub_p)
print(xs.astype('M8[D]'))

mp.grid(linestyle=':')
mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()
