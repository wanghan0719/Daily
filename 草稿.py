import numpy as np
a = np.random.normal(3,2,size=(3,3))
print(a)
print(a.size)
for i in range(len(a)):
    print(a[i,],type(a[i,]))
