import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d


# 3D图像绘制
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标，组成二维数组
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
mp.figure('3d scatter', facecolor='lightgray')
mp.title('3d scatter', fontsize=16)
ax3d = mp.gca(projection='3d')
ax3d.plot_surface(x, y, z, rstride=30,cstride=30,cmap='jet')
ax3d.set_xlabel('x',fontsize=17)
ax3d.set_ylabel('y',fontsize=17)
ax3d.set_zlabel('z',fontsize=17)
mp.show()
