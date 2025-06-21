import math
from functools import reduce

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
a.sort()

l = []
for i in range(n):
    l.append(a[i+1] - a[i])

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

print(gcd_list(l))

