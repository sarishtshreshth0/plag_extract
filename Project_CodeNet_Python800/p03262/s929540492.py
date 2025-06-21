import math
from functools import reduce
N, X = map(int, input().split())
x = list(map(int,input().split()))
 
for i in range(N):
    x[i] = abs(x[i]-X)
 
x = sorted(x)[::-1]
cnt = 0
 
for i in range(N):
    cnt = math.gcd(cnt, x[i])
 
print(cnt)