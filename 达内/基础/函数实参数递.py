def fun01(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)

list01 = [2,1,3]
list02 = (2,1,3)
list03= {2,1,3}
dict01 = {'p1':2,'p2':1,'p3':3,'p4':4}
str01 = "孙悟空"
set01 = {'A','B','C'}
fun01(2,1,3)    #2,1,3   位置实参
fun01(*list01)  # 2,1,3   序列实参
fun01(*list02)  #2,1,3   序列实参
fun01(*list03)  #1,2,3    序列实参
fun01(*dict01)  #a,b,c
fun01(*str01)     #孙，悟，空
fun01(*set01)
fun01(1,p2=2,p3=3) # 位置参数在前，关键字参数在后   关键字实参
fun01(**dict01)   #字典实参
