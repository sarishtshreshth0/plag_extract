import bisect
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)
  

n, x = map(int,input().split())
a = list(map(int,input().split()))

index = bisect.bisect_left(a, x)
a.insert(index, x)
d = [0]*(n)
for i in range(n):
    d[i] = a[i+1] - a[i]
ans = gcd(*d)
print(ans)