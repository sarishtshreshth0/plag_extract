import numpy as np
n=int(input())
a=list(map(int,input().split()))

b=list(np.array(a)+1)
c=list(np.array(a)+2)
a=a+b+c

d=np.argmax(np.bincount(a))
print(a.count(d))