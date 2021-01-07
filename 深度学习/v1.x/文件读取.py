# 利用读取器读取cvs文件
import tensorflow as tf
import os


# tf.compat.v1.disable_eager_execution()

# 定义读取函数：构建文件队列，定义读取器，读取内容，解码内容，批处理
def csv_reader(filelist):  # filelist文件列表
    # 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 定义读取器，从文件队列中读取文件内容
    reader = tf.TextLineReader()  # 文本读取器
    k, v = reader.read(file_queue)  # 读取返回文件名及读到的数据
    # 解码
    records = [['None'], ['None']]  # 默认值
    example, label = tf.decode_csv(v, record_defaults=records)
    # 批处理，分批返回数据
    example_bat, label_bat = tf.train.batch([example, label], batch_size=9, num_threads=1, capacity=9)
    return example_bat, label_bat


if __name__ == '__main__':
    filepath = '../data/test_data'
    file_name = os.listdir(filepath)
    file_list = [filepath + '/' + i for i in file_name]
    print(file_list)

    # 调用csv_read函数，构建队列，读取文件并返回
    example, label = csv_reader(file_list)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()  # 线程协调器，管理线程
        # 创建一组线程
        threads = tf.train.start_queue_runners(sess, coord=coord)
        # 执行读取文件op
        print(sess.run([example, label]))  # 执行这两个op

        # 回收线程
        coord.request_stop()
        coord.join(threads=threads)
