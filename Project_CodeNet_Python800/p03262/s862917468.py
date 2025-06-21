import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

a,b=map(int, input().split())
c=list(map(int, input().split()))
c = c + [b]
d = sorted(c)
l = []

for i in range(a):
    l += [d[i+1] - d[i]]

f=gcd_list(l)
print(f)