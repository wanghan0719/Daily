# CalStatisticsV1.py
def getNum():
    nums = []
    iNumStr = input("请输入数值（回车结束）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数值（回车结束）：")
    return nums


def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s/len(numbers)


def dev(number, mean):
    sdev = 0.0
    for num in number:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(number) - 1), 0.5)


def midian(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


n = getNum()
m = mean(n)
print("平均值：%.2f，方差：%.2f，中位数：%.2f" % (m, dev(n, m), midian(n)))
