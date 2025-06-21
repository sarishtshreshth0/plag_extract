from itertools import accumulate
from collections import Counter
N = int(input())

c = Counter(accumulate(map(int,input().split())))
c[0] += 1

print(sum(k*(k-1)//2 for k in c.values()))