import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


class FashionMnist:
    out_feature1 = 12  # 第一层卷积输出数量
    out_feature2 = 24  # 第2层卷积输出数量
    con_neurons = 512  # 全连接层神经元数量

    def __init__(self, path):
        self.sess = tf.Session()
        self.data = read_data_sets(path,one_hot=True)
        self.tt= None
    # 权重初始化函数
    def
        pass

    # 偏置初始化函数

    # 二维卷积函数
    def cov_2d(self):
        pass
