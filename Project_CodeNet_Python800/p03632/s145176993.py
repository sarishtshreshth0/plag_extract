import numpy as np
a,b,c,d = map(int,input().split())
t = [0]*101

t[a] += 1
t[b] -= 1
t[c] += 1
t[d] -= 1

t = list(np.cumsum(t))
#print(t)
print(t.count(2))