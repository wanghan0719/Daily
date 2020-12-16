import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.metrics as sm

x = np.loadtxt('../data/multiple3.txt', delimiter=',', unpack=False)

# 训练Kmeans模型
bw = sc.estimate_bandwidth(x, n_samples=len(x), quantile=0.1)
model = sc.MeanShift(bandwidth=bw, bin_seeding=True)
model.fit(x)
centers = model.cluster_centers_
pred_y = model.labels_

"""
轮廓系数
    轮廓系数的区间为：[-1, 1]。 -1代表分类效果差，1代表分类效果好。0代表聚类重叠，没有很好的划分聚类。
"""
# 轮廓系数评估聚类模型
score = sm.silhouette_score(x, pred_y, metric='euclidean', sample_size=len(x))
print('聚类模型轮廓系数为：', score)

n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x = np.meshgrid(np.linspace(l, r, n),
                     np.linspace(b, t, n))
flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
mp.figure('K-Means Cluster', facecolor='lightgray')
mp.title('K-Means Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray', shading='auto')
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg_r', s=80, label='Samples')
mp.scatter(centers[:, 0], centers[:, 1], marker='+', c='gold', s=1000, linewidth=1)
mp.legend()
mp.show()
