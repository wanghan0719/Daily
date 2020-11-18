# 查找单词的功能
def find_word(word):
    # 默认r方式打开
    f = open('dict.txt')

    # 每次取一行
    for line in f:
        # 提取一行中的单词
        tmp = line.split(' ')[0]
        # 遍历的单词已经比目标大了
        if tmp > word:
            f.close()
            return "没有找到该单词"
        elif tmp == word:
            f.close()
            return line
    else:
        f.close()
        return "没有找到该单词"


word = input("请输入要查找的单词：")
print(find_word(word))