import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 调整警告级别
tf.compat.v1.disable_eager_execution()
# 创建数据
x = tf.compat.v1.random_normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
y_true = tf.matmul(x, [[2.0]]) + 5.0  # 矩阵相乘必须是二维的

# 第二步：建立线性回归模型
# 建立模型时，随机建立权重、偏置 y = wx + b
# 权重需要不断更新，所以必须是变量类型. trainable指定该变量是否能随梯度下降一起变化
weight = tf.Variable(tf.compat.v1.random_normal([1, 1]), name='w', trainable=True)  # 训练过程中值是否允许变化
bias = tf.Variable(0.0, name='b', trainable=True)  # 偏置
y_pred = tf.matmul(x, weight) + bias  # 计算 wx + b

# 第三步：求损失函数，误差(均方差)
loss = tf.compat.v1.reduce_mean(tf.compat.v1.square(y_true - y_pred))

# # 第四步：使用梯度下降法优化损失
# 学习率是比价敏感的参数，过小会导致收敛慢，过大可能导致梯度爆炸
train_op = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)

# 收集损失值
tf.compat.v1.summary.scalar('losses', loss)
merged = tf.compat.v1.summary.merge_all()  # 将所有的摘要信息保存到磁盘，执行摘要合并

init_op = tf.compat.v1.global_variables_initializer()  # 初始化操作

saver = tf.compat.v1.train.Saver()
with tf.compat.v1.Session() as sess:  # 通过Session运行op
    sess.run(init_op)  # 执行变量初始化

    # 指定事件文件
    fw = tf.compat.v1.summary.FileWriter("summary", graph=sess.graph)  # 定义文件写入器

    # 判断模型文件是否存在，存在则加载，不存在则创建
    if os.path.exists('model/linear_model/checkpoint'):  # 模型已存在
        saver.restore(sess, 'model/linear_model/')  # 加载模型

    # 打印初始权重、偏移值
    print("start training weight==>weight:", weight.eval(), " bias:", bias.eval())
    
    for i in range(200):  # 循环执行训练
        sess.run(train_op)  # 执行训练
        summary = sess.run(merged)  # 执行摘要合并（收集变量，编码）
        fw.add_summary(summary, i)  # 写入第i次收集摘要信息
        print(i, ":", i, "weight:", weight.eval(), " bias:", bias.eval())
    # 训练完成，保持模型
    saver.save(sess, 'model/linear_model/')  # 保存模型
