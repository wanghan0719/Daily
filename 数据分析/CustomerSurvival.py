import numpy as np
import matplotlib.pyplot as mp

index, pack_type, extra_time, extra_flow, use_month, loss = \
    np.loadtxt('data/CustomerSurvival.csv',
               delimiter=',',
               usecols=(0, 1, 2, 3, 4, 5),
               unpack=True,
               dtype='i8,i8,f8,f8,f8,bool',
               skiprows=1)

# 统计额外剩余时长，额外剩余流量，使用月份三个字段的 最小值，最大值，平均值，做出业务分析。
print('-' * 100)
print('额外剩余时长 最大值：{}，最小值：{}，平均值：{}'.format(np.max(extra_time), np.min(extra_time), np.average(extra_time)))
print('额外剩余流量 最大值：{}，最小值：{}，平均值：{}'.format(np.max(extra_flow), np.min(extra_flow), np.average(extra_flow)))
print('使用月份 最大值：{}，最小值：{}，平均值：{}'.format(np.max(use_month), np.min(use_month), np.average(use_month)))

# 统计所有有额外剩余通话时长的人数占总人数的比例。 统计所有有额外剩余流量的人数占总人数的比例。
print('-' * 100)
extra_time_mask = extra_time > 0
print('所有有额外剩余通话时长的人数占总人数的比例为：', extra_time[extra_time_mask].size / extra_time.size)
extra_flow_mask = extra_time > 0
print('所有有额外剩余流量的人数占总人数的比例为：', extra_flow[extra_flow_mask].size / extra_flow.size)

# 统计所有把流量用超了的人们的平均套餐使用月数。
print('-' * 100)
print("所有把流量用超了的人们的平均套餐使用月数为：", np.mean(use_month[extra_flow < 0]))

# 按列进行统计学指标分析（均值，最值，标准差等），结合业务得到相关结论。
print('-' * 100)


def apply(ary):
    return np.mean(ary), np.max(ary), np.min(ary), np.std(ary)


print('平均：{}，最大：{}，最小：{}，标准差：{}'.format(*apply(extra_time)))
print('平均：{}，最大：{}，最小：{}，标准差：{}'.format(*apply(extra_flow)))
print('平均：{}，最大：{}，最小：{}，标准差：{}'.format(*apply(use_month)))

# 绘制散点图，观察套餐额外剩余流量与用户是否流失之间的关系，结合业务得到相关结论。
mp.figure('flow & loss', facecolor='lightgray')
mp.title('flow & loss', fontsize=16)
# mp.grid(linestyle=':')
mp.xlabel('flow', fontsize=14)
mp.ylabel('loss', fontsize=14)
mp.scatter(extra_flow, loss, c=loss, cmap='jet', label='flow & loss', s=50, alpha=0.8)
mp.legend()

# 绘制散点图，观察套餐额外剩余通话时长与用户是否流失之间的关系，结合业务得到相关结论。
mp.figure('time & loss', facecolor='lightgray')
mp.title('time & loss', fontsize=16)
# mp.grid(linestyle=':')
mp.xlabel('time', fontsize=14)
mp.ylabel('loss', fontsize=14)
mp.scatter(extra_time, loss, c=loss, cmap='jet', label='time & loss', s=50, alpha=0.8)
mp.legend()

# 获取所有非流失用户，绘制散点图，观察这些用户额外剩余流量(x)与额外剩余通话时长(y)之间的关系。
mp.figure('extra_flow & extra_time', facecolor='lightgray')
mp.title('extra_flow & extra_time', fontsize=16)
# mp.grid(linestyle=':')
mp.xlabel('extra_flow', fontsize=14)
mp.ylabel('extra_time', fontsize=14)
mp.scatter(extra_flow[loss == 0], extra_time[loss == 0], c=extra_time[loss < 1], cmap='jet', label='extra_flow & extra_time', s=50,
           alpha=0.8)
mp.legend()

# 使用数学模型拟合上一题的数据分布，尝试通过用户额外剩余流量(x)来预测该用户的额外剩余通话时长(y)。
print('-' * 100)
# （一）基于线性模型预测：
A = np.column_stack((extra_flow, np.ones(extra_flow.size)))
B = extra_time
x= np.linalg.lstsq(A,B,rcond=None)[0]
# 预测用户额外流量剩余500时，该用户的额外剩余通话时长是多少？
r = x[0]*500+x[1]
print('用户额外流量剩余500时，该用户的额外剩余通话时长是:',r)


# （二）基于概率分布规律预测：
# 由散点图的分布可知，数据分布大致服从正态分布，可以依据正态分布规律做简单预测。
# 分别求出两组数据的期望与标准差：
print('-' * 100)
flow_E = np.mean(extra_flow)
flow_S = np.std(extra_flow)
time_E = np.mean(extra_time)
time_S = np.std(extra_time)
# 预测可以使用基于正态分布的随机数，通过上述参数做出简单预测。
# 预测10次extra_flow
print(np.random.normal(flow_E, flow_S, 10))
print(np.random.normal(time_E, time_S, 10))

# mp.grid(linestyle=':')
mp.show()
