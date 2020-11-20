import matplotlib.pyplot as mp
import matplotlib.animation as ma
import numpy as np

n = 100
bubbles = np.zeros(n, dtype=[('position', 'f8', 2),
                             ('size', 'f8', 1),
                             ('growth', 'f8', 1),
                             ('color', 'f8', 4)])

bubbles['position'] = np.random.uniform(0, 1, (n, 2))  # 产生均匀位置
bubbles['size'] = np.random.uniform(40, 70, n)  # 生成大小，40-70之间
bubbles['growth'] = np.random.uniform(10, 20, (n, 2))  # 增长值，10-20之间
bubbles['color'] = np.random.uniform(0, 1, (n, 4))  # 生成颜色，范围0-1，R,G,B,Alpha


# 简单动画
def update(number):
    #

    bubbles['size'] += bubbles['growth']
    bubbles['size'] += bubbles['growth']  # 增加气泡大小
    # 每次执行update时，选择一个点，让它重新初始化属性（破裂）
    ind = number % 100
    bubbles[ind]['size'] = np.random.uniform(40, 70, 1)
    bubbles[ind]['position'] = np.random.uniform(0, 1, (1, 2))
    anim.set_sizes(bubbles['size'])  # 重新设置大小
    anim.set_offsets(bubbles['position'])  # 设置偏移位置


mp.figure('Animation', facecolor='lightgray')
anim = ma.FuncAnimation(mp.gcf(), update, interval=20)

mp.show()
