n,*aa = map(int, open(0).read().split())

from itertools import accumulate
from collections import Counter
from math import comb

c = Counter(accumulate(aa))
c[0] += 1

ans = 0
for i,v in c.items():
    if v > 1:
        ans += comb(v,2)

print(ans)