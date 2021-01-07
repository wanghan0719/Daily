import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


class FashionMnist:
    out_feature1 = 12  # 第一层卷积输出数量
    out_feature2 = 24  # 第2层卷积输出数量
    con_neurons = 512  # 全连接层神经元数量

    # 构造函数
    def __init__(self, path):
        self.sess = tf.Session()  # 创建操作
        self.data = read_data_sets(path, one_hot=True)  # 加载数据集
        self.tt = None

    # 权重初始化函数
    def init_weight_variable(self, shape):
        # 创建一个截尾正态分布的随机矩阵
        # 截尾正态分布：产生的随机数不会超过两倍标准差
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    # 偏置初始化函数
    def init_bias_variable(self, shape):
        initial = tf.constant(1.0, shape=shape)
        return tf.Variable(initial)

    # 二维卷积函数
    def cov_2d(self, x, w):
        # input : 输入数据[batch, in_height, in_width, in_channels]
        # filter : 卷积窗口[filter_height, filter_width, in_channels, out_channels]
        # strides: 卷积核每次移动步数，对应着输入的维度方向
        # padding='SAME' ： 输入和输出的张量形状相同
        return tf.nn.conv2d(x, w,
                            strides=[1, 1, 1, 1],  # 每个维度上的步长值
                            padding='SAME')

    # 池化函数
    def max_pool_2x2(self, x):
        return tf.nn.max_pool(x,
                              ksize=[1, 2, 2, 1],  # 每个维度上池划区域的大小
                              strides=[1, 2, 2, 1],  # 每个维度上的步长值
                              padding='SAME')

    # 构建卷积/激活/池化组函数
    def create_conv_pool_layer(self, input, input_features, out_features):
        filter = self.init_weight_variable([5, 5, input_features, out_features])  # 卷积核
        b_conv = self.init_bias_variable([out_features])  # 偏置,个数等于卷积输出值的个数
        # 做卷积池化计算
        h_conv = tf.nn.relu(self.cov_2d(input, filter) + b_conv)
        # 做池化操作
        h_pool = self.max_pool_2x2(h_conv)
        return h_pool

    # 构建全连接函数
    def create_fc_layer(self, h_pool_flat, input_features, con_neurons):
        w_fc = self.init_weight_variable([input_features, con_neurons])  # 权重
        b_fc = self.init_bias_variable([con_neurons])  # 偏置
        # 执行wx+b计算
        h_fc1 = tf.nn.relu(tf.matmul(h_pool_flat, w_fc) + b_fc)
        return h_fc1

    # 构建CNN函数
    def build(self):
        # 输入
        self.x = tf.placeholder(tf.float32, shape=[None, 784])
        x_image = tf.reshape(self.x, [-1, 28, 28, 1])  # 设置形状28*28
        self.y = tf.placeholder(tf.float32, shape=[None, 10])  # 真是类别[1,0,0,0,0,0,0,0,0,0]

        # 第一组卷积/激活/池化
        h_pool1 = self.create_conv_pool_layer(x_image,  # 输入原始图像数据
                                              1,  # 输入特征个数
                                              self.out_feature1)  # 输出特征数量
        # 第二组卷积/激活/池化
        h_pool2 = self.create_conv_pool_layer(h_pool1,  # 第一组卷积池化层的输出作为输入
                                              self.out_feature1,  # 输入特征个数等于上一层输出特征数
                                              self.out_feature2)  # 输出特征数量
        # 全连接层
        h_pool2_flat_features = 7 * 7 * self.out_feature2  # 计算总的特征个数
        h_pool2_flat = tf.reshape(h_pool2, [-1, h_pool2_flat_features])  # 变维：变成一维
        h_fc = self.create_fc_layer(h_pool2_flat, h_pool2_flat_features, self.con_neurons)

        # Dropout
        self.keep_prob = tf.placeholder('float')  # 丢弃率
        h_fc1_drop = tf.nn.dropout(h_fc, self.keep_prob)

        # 输出层（全连接层）
        w_fc = self.init_weight_variable([self.con_neurons, 10])
        b_fc = self.init_bias_variable([10])
        y_conv = tf.matmul(h_fc1_drop, w_fc) + b_fc

        # 计算准确率
        correct_pred = tf.equal(tf.argmax(y_conv, 1), tf.argmax(self.y, 1))
        self.accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))  # 计算准确率

        # 构建损失函数
        loss_func = tf.nn.softmax_cross_entropy_with_logits(labels=self.y,  # 真实结果
                                                            logits=y_conv)  # 预测结果
        cross_entropy = tf.reduce_mean(loss_func)

        # 优化器
        optimizer = tf.train.AdamOptimizer(0.001)  # 自适应梯度优化器
        self.train_step = optimizer.minimize(cross_entropy)

    # 训练函数
    def train(self):
        self.sess.run(tf.global_variables_initializer())  # 初始化变量
        merged = tf.summary.merge_all()  # 摘要合并
        batch_size = 100
        print('begging training...')

        for i in range(10):  # 循环执行训练
            total_batch = int(self.data.train.num_examples / batch_size)  # 计算批次
            for j in range(total_batch):
                batch = self.data.train.next_batch(batch_size)  # 获取一个批次训练样本数据
                # 参数：图像，标签，丢弃率
                params = {self.x: batch[0], self.y: batch[1], self.keep_prob: 0.5}

                t, acc = self.sess.run([self.train_step, self.accuracy], feed_dict=params)  # 要执行的op
                if j % 100 == 0:
                    print('i:%d, j:%d,acc:%f' % (i, j, acc))

    # 评价函数
    def eval(self, x, y, keep_prod):
        params = {self.x: x, self.y: y, self.keep_prob: keep_prod}
        test_acc = self.sess.run(self.accuracy, params)  # 使用测试数据计算准确率
        print("test accuracy:%f" % test_acc)
        return test_acc

    # 关闭会话
    def close(self):
        self.sess.close()


if __name__ == "__main__":
    mnist = FashionMnist('../data/fashion_mnist')
    mnist.build()  # 搭建模型
    mnist.train()  # 执行训练

    print('\n----- Test -----')
    xs, ys = mnist.data.test.next_batch(100)  # 从测试集读取100个样本
    mnist.eval(xs, ys, 0.5)
    mnist.close()
