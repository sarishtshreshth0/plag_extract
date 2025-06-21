import sys
import math
from collections import Counter

N = input()
l = list(map(int, input().split()))
accum  = [0]
for n in l:
    accum.append(accum[-1] + n)
c = Counter(accum)

print(sum(math.comb(v, 2) for v in c.values()))