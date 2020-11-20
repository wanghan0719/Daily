import matplotlib.pyplot as mp
import matplotlib.animation as ma

number =0
# 简单动画
def update(number):
    print(number)
    number+=1


mp.figure('Animation')
anim = ma.FuncAnimation(mp.gcf(), update, interval=20)
mp.show()
