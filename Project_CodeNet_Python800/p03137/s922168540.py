import numpy as np
n,m=map(int,input().split())
x=list(map(int,input().split()))

arr=np.sort(np.array(x))
dif=np.diff(arr)

lis=dif.tolist()
lis=sorted(lis)

for i in range(n-1):
    if len(lis)>0:
        lis.pop()

print(sum(lis))