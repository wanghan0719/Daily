# percetron 自定义感知机
# 感知和
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7  # 权重1，权重2，阈值
    tmp = x1 * w1 + x2 * w2  # 做线性计算
    if tmp > theta:
        return 1
    else:
        return 0


# 感知或
def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2  # 权重1，权重2，阈值
    tmp = x1 * w1 + x2 * w2  # 做线性计算
    if tmp > theta:
        return 1
    else:
        return 0


# 利用多层感知机实现异或
def XOR(x1, x2):
    s1 = not AND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print(AND(1, 1))
print(AND(0, 1))

print(OR(0, 1))
print(OR(1, 1))

print(XOR(1, 0))
print(XOR(1, 1))
