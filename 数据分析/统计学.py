import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    dat = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    tm = dat.strftime("%Y-%m-%d")  # 格式化
    return tm


dates, opening_price, highest_price, lowest_price, closing_price = np.loadtxt('data/aapl.csv', delimiter=',',
                                                                              usecols=(1, 3, 4, 5, 6), unpack=True,
                                                                              dtype='M8[D],f8,f8,f8,f8',
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
mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()  # 自动格式化当前X轴刻度
mp.show()
