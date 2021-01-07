import tensorflow as tf
import os
import pylab
from tensorflow.keras.datasets.mnist import load_data

tf.compat.v1.disable_eager_execution()

# 准备数据，定义占位符
mnist = tf.keras.datasets.mnist.load_data()
print(len(mnist))
x = tf.compat.v1.placeholder(tf.float32, [None, 784])  # 输入数据，N张图片，每张图片784特征（像素）
y = tf.compat.v1.placeholder(tf.float32, [None, 10])  # 输出数据，N个样本的预测结果，每个样本10个预测值

w = tf.compat.v1.Variable(tf.compat.v1.random_normal([784, 10]))  # 权重
b = tf.compat.v1.Variable(tf.compat.v1.zeros([10]))  # 偏置，10个输出对应10个偏置

# 搭建模型，全连接模型，构建损失函数，定义优化
pred_y = tf.compat.v1.nn.softmax(tf.compat.v1.matmul(x, w) + b)  # 计算输出，并且交给softmax激活函数
cross_entropy = -tf.compat.v1.reduce_sum(y * tf.compat.v1.log(pred_y),
                                         reduction_indices=1)  # 求交叉熵
cost = tf.compat.v1.reduce_mean(cross_entropy)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cost)  # 梯度下降优化器

# 执行训练，模型保存
train_epochs = 20  # 训练轮次
batch_size = 100  # 批次大小
saver = tf.compat.v1.train.Saver()
model_path = 'model/mnist/mnist_model.ckpt'  # 模型路径

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())  # 初始化
    # 循环训练
    for i in range(train_epochs):
        avg_cost = 0.0
        # total_batch = int(mnist.train.num_examples / batch_size)
# 模型测试r
tf.argmax()
