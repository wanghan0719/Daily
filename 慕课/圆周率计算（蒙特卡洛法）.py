# CalPi.py
from random import random
from time import perf_counter

DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS + 1):
    X, Y = random(), random()
    dist = pow((pow(X, 2) + pow(Y, 2)), 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
print(f"圆周率为：{pi}")
print("运行时间是：{:.5f}".format(perf_counter() - start))
