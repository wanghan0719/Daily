import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.gridspec as mg
import matplotlib.pyplot as mp
import numpy as np
import cv2 as cv

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 6, 9, 12, 15])
mp.plot(x, y)

# 绘制水平线与垂直线
mp.hlines(60, 2, 5)  # y值为60，x从2到5
mp.hlines([60, 70, 80], 2, 5)
mp.hlines([60, 70, 80], [2, 3, 4], [5, 6, 7])
mp.vlines(4, 10, 70, linestyles='--', colors=(0.9, 0.3, 0.2), )
mp.show()

# 绘制正弦曲线
x = np.linspace(0, 2 * math.pi, 1000)

sinx = np.sin(x)
mp.plot(x, sinx, linestyle='--', linewidth=2, color='orangered',
        alpha=0.8, label=r'$y=sinx$')

cosx = np.cos(x)
mp.plot(x, cosx, label=r'$y=cosx$')

# 设置坐标刻度
mp.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
          ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])

# 设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 添加图例
mp.legend(loc='best')

# 设置特殊点
mp.scatter([np.pi / 2, np.pi / 2], [0, 1], marker='o', s=80,
           edgecolors='red', facecolor='green', label='Points', zorder=3)

# 添加备注
mp.annotate(
    r'$[\frac{\pi}{2},1]$',  # 备注中显示的文本内容
    xycoords='data',  # 备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(np.pi / 2, 1),  # 备注目标点的坐标 (4,16)
    textcoords='offset points',  # 备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(50, 30),  # 备注文本的坐标
    fontsize=14,  # 备注文本的字体大小
    arrowprops=dict(
        arrowstyle="->", connectionstyle="angle3"
    )  # 使用字典定义文本指向目标点的箭头样式
)
mp.show()

mp.figure('Apple', facecolor='lightgray')
x = np.arange(0, 5, 0.01)
y = x ** 2
mp.plot(x, y)
mp.xlabel('t', fontsize=16)
mp.ylabel('v', fontsize=16)
mp.grid(linestyle='--')

mp.figure('Orange', facecolor='gray')
x = np.arange(0, 6, 0.01)
y = -x ** 2
mp.plot(x, y)
mp.xlabel('t', fontsize=16)
mp.ylabel('s', fontsize=16)
mp.grid(linestyle=':')
mp.show()

# 矩阵布局
mp.figure('Subplot', facecolor='yellow')
for i in range(9):
    mp.subplot(3, 3, i + 1)
    mp.text(0.5, 0.5, i, ha='center', va='center', size=36, alpha=0.5)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout(pad=2, h_pad=2, w_pad=2)
mp.show()

# 网格布局
mp.figure('Grid spec', facecolor='blue')
gs = mg.GridSpec(3, 3)

mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[:2, 2])
mp.text(0.5, 0.5, 2, ha='center', va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, 3, ha='center', va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1:, 0])
mp.text(0.5, 0.5, 4, ha='center', va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[-1, 1:])
mp.text(0.5, 0.5, 5, ha='center', va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()

# 自由布局
mp.figure('Flow layout', facecolor='pink')
mp.axes([0.03, 0.03, 0.94, 0.94])
mp.text(0.5, 0.5, 'H', size=40, alpha=0.9)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()

# 刻度定位器
mp.figure('Locator', facecolor='lightgreen')
mp.title('Locator', fontsize=36)
# 处理坐标轴
ax = mp.gca()
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 修改x轴的刻度定位器
# ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_major_locator(mp.AutoLocator())
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.xlim(1, 10)
ax.spines['bottom'].set_position(('data', 0.5))
mp.show()

locators = ['mp.NullLocator()',  # 空刻度定位器，不绘制刻度
            'mp.MultipleLocator(1)',  # 多点定位器：从0开始，按照参数指定的间隔(缺省1)绘制
            'mp.MaxNLocator(nbins=4)',  # 最多绘制指定个数+1个主刻度
            'mp.AutoLocator()']  # 自动定位器：由系统自动选择刻度的绘制位置

for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i + 1, facecolor='lightblue')
    mp.xlim(0, 10)
    mp.ylim(-1, 1)
    mp.yticks([])
    # 获取当前坐标轴
    ax = mp.gca()
    # 隐藏除底轴以外的所有坐标轴
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # 将底坐标轴调整到子图中心位置
    ax.spines['bottom'].set_position(('data', 0))
    # 设置水平坐标轴的主刻度定位器
    ax.xaxis.set_major_locator(eval(locator))
    # 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
    mp.plot(np.arange(11), np.zeros(11), c='none')
    # 标记所用刻度定位器类名
    mp.text(5, 0.3, locator, ha='center', size=12)

mp.show()

# 散点图
n = 100
x = np.random.normal(175, 5, n)
y = np.random.normal(60, 8, n)
mp.figure('Scatter', facecolor='lightpink')
mp.title('Scatter', fontsize=37)
# mp.scatter(x, y, color='lightblue', s=80, alpha=0.5, label='Persons',
#            marker='o')
d = (x - 175) ** 2 + (y - 60) ** 2
mp.scatter(x, y, c=d, s=80, alpha=0.5, label='Persons',
           marker='o', cmap='rainbow')
mp.legend()
mp.show()

# 填充
x = np.linspace(0, 8 * np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2
mp.figure('Fill', facecolor='lightyellow')
mp.title('Fill', fontsize=36)
mp.plot(x, sinx, color='dodgerblue', linestyle='--', label=r'$y=sin(x)$')
mp.plot(x, cosx, color='orangered', label=r'$y=\frac{cos(frac{x}{2})}{2}$')
# 填充闭合区域
mp.fill_between(x, sinx, cosx, sinx > cosx, color='lightgreen', alpha=0.3)
mp.fill_between(x, sinx, cosx, sinx < cosx, color='orangered', alpha=0.3)
mp.legend()
mp.show()

# 柱状图

apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar', fontsize=36)
mp.xlabel('month', fontsize=20)
mp.ylabel('quantity', fontsize=20)
mp.grid(linestyle=':', axis='y')
x = np.arange(len(apples))
mp.bar(x - 0.2, apples, width=0.4, color='pink', label='apple', alpha=0.8)
mp.bar(x + 0.2, oranges, width=0.4, color='orange', label='orange', alpha=0.8)
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()

# 直方图
img = cv.imread('data/lyf.jpg', flags=0)
# print(img.shape, img[0][0])
# 绘制统计直方图
mp.figure("Hist", facecolor='lightpink')
mp.title('Hist', fontsize=16)
mp.hist(img.ravel(), bins=10, color='green', edgecolor='white', range=(0, 255), density=True)
mp.xticks(np.linspace(0, 255, 11))
mp.show()

# 饼状图
values = [15, 13.3, 8.5, 7.3, 4.62, 51.28]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01, 0.01]
labels = ['Java', 'C', 'Python', 'C++', 'VB', 'Other']
colors = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold', 'blue']
mp.figure('Pie', facecolor='lightgray')
mp.axis('equal')
mp.pie(values, spaces, labels, colors, '%.1f%%', shadow=True, startangle=0, radius=1)  # 绘制饼图
mp.legend(loc='lower right')
mp.show()

# 等高线图
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标，组成二维数组
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# 绘制等高线
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=17)
mp.grid(linestyle=':')
cntr = mp.contour(x, y, z, 8, colors='black', linewidths=0.5)  # 绘制等高线图
# 为等高线添加标签
mp.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)
# 填充等高线
cntr = mp.contourf(x, y, z, 8, cmap='jet')
mp.show()

# 热图
img = cv.imread('data/lyf.jpg', flags=0)
mp.figure('Colorbar', facecolor='lightgray')  # ColorBar:热成像图
mp.title('Color')
mp.imshow(img, cmap='gray')
mp.colorbar()  # 显示边条
mp.show()

# 3D图像绘制


# 3d散点图
n = 200
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

mp.figure('3D Scatter')
ax3d = mp.gca(projection='3d')
mp.title('3D Scatter', fontsize=16)
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
d = x ** 2 + y ** 2 + z ** 2
ax3d.scatter(x, y, z, s=80, alpha=0.7, marker='o', c=d, cmap='jet')
mp.show()

# 绘制3d曲面图
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标，组成二维数组
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
mp.figure('3d surface', facecolor='lightgray')
mp.title('3d surface', fontsize=16)
ax3d = mp.gca(projection='3d')
ax3d.plot_surface(x, y, z, rstride=30, cstride=30, cmap='jet')
ax3d.set_xlabel('x', fontsize=17)
ax3d.set_ylabel('y', fontsize=17)
ax3d.set_zlabel('z', fontsize=17)
mp.show()

# 3d线框图
n = 500
# 生成网格化坐标矩阵中所有坐标的x与所有坐标的y
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
# 通过坐标矩阵中每个坐标的x与y，计算当前坐标的高度值z，组成二维数组
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# z会把每个坐标点的x与y取出，计算结果作为坐标点的高度值 得到n*n的一个二维数组
mp.figure('3d wireframe')
ax3d = mp.gca(projection='3d')
mp.title('3d surface', fontsize=16)
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
ax3d.plot_wireframe(x, y, z, cstride=20, rstride=20, cmap='jet')
mp.tight_layout()
mp.show()
