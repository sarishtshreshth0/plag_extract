def lin(x,y):
    return np.sqrt(sum((x-y)**2))

from itertools import combinations as cb
n,d = map(int,input().split())
import numpy as np

x=[]
for i in range(n):
    x.append(np.array(list(map(int,input().split()))))

cnt = 0
for a,b in cb(range(n),2):
    #print(x[a],x[b])
    if lin(x[a],x[b]).is_integer():
        cnt += 1

print(cnt)