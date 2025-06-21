from itertools import product
from bisect import bisect_left, bisect_right

n = int(input())
s = []
for i in range(3, 10):
    for v in product('753', repeat=i):
        if len(set(v)) >= 3:
            s.append(int(''.join(v)))

s.sort()

idx = bisect_right(s, n)
print(len(s[:idx]))