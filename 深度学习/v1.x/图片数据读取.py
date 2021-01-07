import tensorflow as tf
import os
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 调整警告级别


# 定义图片读取函数
def img_reader(filelist):  # filelist文件列表
    # 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 定义读取器，从文件队列中读取文件内容
    reader = tf.WholeFileReader()  # 文本读取器
    k, v = reader.read(file_queue)  # 读取返回文件名及读到的数据
    # 解码
    img = tf.image.decode_jpeg(v)
    img_resize = tf.image.resize_images(img, size=[200, 200])
    img_resize.set_shape([200, 200, 3])  # 固定样本形状，批处理时对形状有要求，修改张量的静态形状
    # 批处理，分批返回数据
    img_bat = tf.train.batch([img_resize], batch_size=10, num_threads=1)
    return img_bat


if __name__ == '__main__':
    filepath = '../data/test_img'
    file_name = os.listdir(filepath)
    file_list = [filepath + '/' + i for i in file_name]
    print(file_list)

    # 调用csv_read函数，构建队列，读取文件并返回
    img = img_reader(file_list)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()  # 线程协调器，管理线程
        # 创建一组线程
        threads = tf.train.start_queue_runners(sess, coord=coord)
        # 执行读取文件op
        # print(sess.run(img))  # 执行这两个op
        imgs = img.eval()

        # 回收线程
        coord.request_stop()
        coord.join(threads=threads)
# 显示图片
plt.figure('img show', facecolor='gray')
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgs[i].astype('int32'))  # 显示第i张图片

plt.tight_layout()
plt.show()
