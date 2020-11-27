import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
import datetime as dt

dates, opening_price, highest_price, lowest_price, closing_price, ma5, ma10 = np.loadtxt \
    ('data/pfyh.csv', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True, dtype='M8[D],f8,f8,f8,f8,f8,f8')
mp.figure('PFYH', facecolor='lightgray')
mp.title('PFYH', fontsize=17)
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
mp.plot(dates, closing_price, color='dodgerblue', linestyle='-', linewidth=2, label='PFYH')


# 定义一个函数，基于均线理论设计投资策略，建议买入返回1，建议卖出返回-1，否则返回0
def profit(param_date):
    # 根据参数日期，基于均线理论返回结果
    mma5 = ma5[dates <= param_date]
    mma10 = ma10[dates <= param_date]
    # 今天的的数据mdates[-1]，昨天的数据mdates[-2]
    if mma5.size < 2:
        return 0
    if (mma5[-2] <= mma10[-2]) and (mma5[-1] >= mma10[-1]):  # 出现金叉
        return 1
    if (mma5[-2] >= mma10[-2]) and (mma5[-1] <= mma10[-1]):  # 出现死叉
        return -1
    return 0


# 矢量化投资函数
vec_func = np.vectorize(profit)
# 使用适量换函数计算收益
profits = vec_func(dates)
print(profits)


# 回测模型
# 定义资产
assets = 1000000
stocks = 0
payment_price = 0
status = 0
for index, profit in enumerate(profits):
    current_price = closing_price[index]
    # 如果是买入并且赔了的状态，若已经跌出5%，则强制卖出
    if status == 1:
        payment_assets = payment_price * stocks
        current_assets = current_price * stocks
        if (payment_assets > current_assets) and ((payment_assets - current_assets) > payment_assets * 0.05):
            payment_price = current_price
            assets = assets + stocks * payment_price
            stocks = 0
            status = -1
            print(
                '止损：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets,
                                                                                    stocks))
    if (profit == 1) and (status != 1):  # 买入
        payment_price = current_price
        stocks = int(assets / payment_price)
        assets = assets - stocks * payment_price
        status = 1
        print('买入：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets,
                                                                                  stocks))
    if (profit == -1) and (status != -1):  # 卖出
        payment_price = current_price
        assets = assets + stocks * payment_price
        stocks = 0
        status = -1
        print('卖出：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets,
                                                                                  stocks))
    print('持有：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets,
                                                                              stocks))

mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()  # 自动格式化当前X轴刻度
mp.show()
