import tensorflow as tf
import os
import pylab
from tensorflow.examples.tutorials.mnist import input_data

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 调整警告级别

# 准备数据，定义占位符
mnist = input_data.read_data_sets('../data/mnist_data', one_hot=True)
print(len(mnist))
x = tf.placeholder(tf.float32, [None, 784])  # 输入数据，N张图片，每张图片784特征（像素）
y = tf.placeholder(tf.float32, [None, 10])  # 输出数据，N个样本的预测结果，每个样本10个预测值

w = tf.Variable(tf.random_normal([784, 10]))  # 权重
b = tf.Variable(tf.zeros([10]))  # 偏置，10个输出对应10个偏置

# 搭建模型，全连接模型，构建损失函数，定义优化
pred_y = tf.nn.softmax(tf.matmul(x, w) + b)  # 计算输出，并且交给softmax激活函数
cross_entropy = -tf.reduce_sum(y * tf.log(pred_y), reduction_indices=1)  # 求交叉熵
cost = tf.reduce_mean(cross_entropy)  # 求损失函数的平均值

# 参数设置
lr = 0.01  # 学习率
optimizer = tf.train.GradientDescentOptimizer(lr).minimize(cost)  # 梯度下降优化器

# 执行训练，模型保存
train_epochs = 20  # 训练轮次
batch_size = 100  # 批次大小
saver = tf.train.Saver()
model_path = '../model/mnist/mnist_model.ckpt'  # 模型路径

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 变量初始化
    # 循环训练
    for epoch in range(train_epochs):
        avg_cost = 0.0
        total_batch = int(mnist.train.num_examples / batch_size)
        # 遍历全数据集
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)  # 读取一个批次样本
            params = {x: batch_xs, y: batch_ys}  # 训练参数
            o, c = sess.run([optimizer, cost], feed_dict=params)  # 执行训练
            avg_cost += (c / total_batch)  # 求平均损失值
        print('epoch: %d, cost: %.9f' % (epoch + 1, avg_cost))
    print('Finished')

    # 模型评估
    correct_pred = tf.equal(tf.argmax(pred_y, 1), tf.argmax(y, 1))
    # 计算准确率
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    print('accuracy:', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
    # 将模型保存到文件
    save_path = saver.save(sess, model_path)
    print('Model saved:', save_path)

# 测试模型
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, model_path)  # 加载模型

    batch_xs, batch_ys = mnist.test.next_batch(2)  # 读取两个测试样本
    output = tf.argmax(pred_y, 1)  # 预测结果值
    output_val, predv = sess.run([output, pred_y],  # 操作
                                 feed_dict={x: batch_xs, y: batch_ys})  # 参数
    print('预测结论：\n', output_val, '\n')
    print('实际结果：\n', batch_ys, '\n')
    print('预测概率：\n', predv, '\n')

    # 显示图片
    im = batch_xs[0]  # 第1个测试样本数据
    im = im.reshape(-1, 28)
    pylab.imshow(im)
    pylab.show()

    im = batch_xs[1]  # 第2个测试样本数据
    im = im.reshape(-1, 28)
    pylab.imshow(im)
    pylab.show()
