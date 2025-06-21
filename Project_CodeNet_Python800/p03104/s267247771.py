#from functools import reduce
from math import log
A,B = map(int, input().split())

def f(x):
    if x <= 0:
        return []
    n = int(log(x,2))
    r = [0 for i in range(n+1)]
    while x > 0:
        n = int(log(x,2))
        for i in range(n):
            r[i] += pow(2,n-1)
        x -= pow(2,n)
        r[n] += x+1
    return r

a = f(A-1)
b = f(B)
for i,v in enumerate(a):
    b[i] -= v

ans = 0
for i,v in enumerate(b):
    if v % 2 == 1:
        ans += pow(2,i)
print(ans)

#print(reduce(lambda x,y:x^y, range(A,B+1)))
