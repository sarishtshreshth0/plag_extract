
import numpy as np

n,x = map(int,input().split())

s = list(map(int,input().split()))

s.append(x)

s.sort()

l = set([])

for i in range(len(s)-1):
    l.add(s[i+1]-s[i])
    
l = list(l)
    
print(np.gcd.reduce(l))