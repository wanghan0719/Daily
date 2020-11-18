"""
使用进程池完成对一个目录的备份,目录中可能有若干的
普通文件,要求把每个文件的拷贝工作作为一个进程事件

     提示:  文件的拷贝函数
           os.listdir() 查看目录下所有文件
           os.mkdir() 创建一个目录

     * plus版  在拷贝的过程中实时打印拷贝的百分比进度
"""
from multiprocessing import Pool, Queue
import os

q = Queue()


# 拷贝文件函数
def copy_file(file, old_file, new_file):
    fr = open(old_file + '/' + file, 'rb')
    fw = open(new_file + '/' + file, 'wb')
    # 开始拷贝
    while True:
        data = fr.read(1024 * 50)
        if not data:
            break
        n = fw.write(data)  # 返回写入多少字节
        q.put(n)  # 放入消息队列
    fr.close()
    fw.close()


def main():
    base_path = '/home/wang/'
    dir = input("请输入要拷贝的目录名：")
    old_folder = base_path + dir
    # 目标位置
    new_folder = old_folder + '-备份'
    os.mkdir(new_folder)
    all_file = os.listdir(old_folder)

    # 计算整个目录的大小
    total_size = 0
    for file in all_file:
        total_size += os.path.getsize(old_folder + '/' + file)

    # 创建进程池
    pool = Pool()
    for file in all_file:
        pool.apply_async(copy_file, args=(file, old_folder, new_folder))
    pool.close()
    copy_size = 0
    while True:
        copy_size += q.get()
        print("拷贝了%.1f%%" % (copy_size / total_size * 100))
        if copy_size >= total_size:
            break
    print("总共拷贝了%.1fK" % (total_size / 1024))
    pool.join()

if __name__ == '__main__':
    main()
