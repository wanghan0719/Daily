# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl
p = [-3, 1, 2, 1]
x = np.linspace(-10, 10, 1000)
y = np.polyval(p, x)
# P = np.polyfit(x, y, 2)
# y1 = np.polyval(P, x)

mpl.figure('nihe', facecolor='gray')
mpl.title("polyfit", fontsize=10)
mpl.plot(x, y, color='red', linestyle=':')

P = np.polyfit(x, y, 2)
y1 = np.polyval(P, x)




mpl.plot(x, y1, color='blue', linestyle='-')
mpl.show()
