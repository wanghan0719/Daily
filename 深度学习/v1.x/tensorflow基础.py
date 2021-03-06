import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 调整警告级别

# hello是一个张量（常量），也是操作（数据计算规则），还没有执行
# hello = tf.constant('hello world')
# print(hello)
# sess = tf.Session()  # 创建session对象
# print(sess.run(hello))  # 执行hello操作
# sess.close()  # 关闭session

# 张量相加实例
# a = tf.constant(5.0)  # 定义张量a（操作）
# b = tf.constant(1.0)  # 定义张量b（操作）
# c = tf.add(a, b)
# print(c)

# 获取默认graph
# graph = tf.get_default_graph()  # 获取缺省图
# print(graph)

# 创建新graph
# graph2 = tf.Graph()
# print(graph2)
# with graph2.as_default():  # 设置默认graph
#     d = tf.constant(11.0)

# with tf.Session(graph=graph2) as sess:
#     print(sess.run(d))
#     print(sess.graph)
#     print(d.shape)
#     print(d.name)
#     print(d.dtype)
#     print(d.op)
# print(sess.run(c))
# print(a.graph)
# print(b.graph)
# print(c.graph)

# 生成值全为0的张量
# tensor_zeros = tf.zeros(shape=[2, 3], dtype="float32")
# 生成值全为1的张量
# tensor_ones = tf.ones(shape=[2, 3], dtype="float32")
# 创建正态分布张量
# tensor_nd = tf.random_normal(shape=[10], mean=1.7, stddev=0.2, dtype="float32")
# 生成和输入张量形状一样的张量，值全为1
# tensor_zeros_like = tf.zeros_like(tensor_ones)

# with tf.Session() as sess:
#     print(tensor_zeros.eval())  # eval表示在session中计算该张量
#     print(tensor_ones.eval())
#     print(tensor_nd.eval())
#     print(tensor_zeros_like.eval())


"""
占位符
"""
# 不确定数据，先使用占位符占个位置
# plhd = tf.placeholder(tf.float32, [2, 3])  # 2行3列的tensor
# plhd2 = tf.placeholder(tf.float32, [None, 3])  # N行3列的tensor

# with tf.Session() as sess:
#     d = [[1, 2, 3],
#          [4, 5, 6]]
#     print(sess.run(plhd, feed_dict={plhd: d}))
#     print("shape:", plhd.shape)
#     print("name:", plhd.name)
#     print("graph:", plhd.graph)
#     print("op:", plhd.op)
#     print(sess.run(plhd2, feed_dict={plhd2: d}))

"""
张量形状改变
"""
# pld = tf.placeholder(tf.float32, [None, 3])
# print(pld)

# pld.set_shape([4, 3])
# print(pld)
# pld.set_shape([3, 3]) #报错，静态形状一旦固定就不能再设置静态形状

# 动态形状可以创建一个新的张量，改变时候一定要注意元素的数量要匹配
# new_pld = tf.reshape(pld, [3, 4])
# print(new_pld)
# new_pld = tf.reshape(pld, [2, 4]) # 报错，元素的数量不匹配

"""
变量&张量
"""
# # 创建普通张量
# a = tf.constant([1, 2, 3, 4, 5])
# # 创建变量
# var = tf.Variable(initial_value=tf.random.normal([2,3]), name='variable')
# # 初始化变量
# init_op=tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init_op)
#     print(sess.run([a, var])) #执行多个op

"""
可视化
"""
''' 变量OP
1. 变量OP能够持久化保存，普通张量则不可
2. 当定义一个变量OP时，在会话中进行初始化
3. name参数：在tensorboard使用的时候显示名字，可以让相同的OP进行区分
'''
# 创建普通张量
a = tf.constant([1, 2, 3, 4, 5])
# 创建变量
var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0),
                  name="variable")

b = tf.constant(3.0, name="a")
c = tf.constant(4.0, name="b")
d = tf.add(b, c, name="add")

# 变量必须显式初始化, 这里定义的是初始化操作，并没有运行
init_op = tf.global_variables_initializer()

# with tf.compat.v1.Session() as sess:
#     sess.run(init_op)
#     # 将程序图结构写入事件文件
fw = tf.summary.FileWriter("summary")
fw.flush()
# print(sess.run([a, var]))




