import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

a = np.array([70, 80, 90])
b = np.array([90, 80, 70])
c = np.corrcoef(a, b)
print(c[0, 1])

# ax = plt.gca()
# axis = ax.spines['left']
# axis.set_position(('data',0))
# axis.set_color('red')
# plt.hlines([60, 70, 80], 2, 5, colors='red', linewidth=3, linestyles=':')
plt.annotate(
    r'$y = x ^ 2$',  # 备注中显示的文本内容
    xycoords='data',  # 备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(4, 16),  # 备注目标点的坐标 (4,16)
    textcoords='offset points',  # 备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(20, 30),  # 备注文本的坐标
    fontsize=14,  # 备注文本的字体大小
    arrowprops=dict(
        arrowstyle="->", connectionstyle="angle3"
    )  # 使用字典定义文本指向目标点的箭头样式
)

plt.show()

import scipy.io.wavfile as wf
sample_rate,noised_sigs=wf.read()
