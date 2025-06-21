#!/usr/bin/env python3
from collections import Counter

n, *d = map(int, open(0).read().split())
c = Counter(d[1:])
c = [(0, 1)] + sorted(c.items())
ans = d[0] == 0
for i in range(1, len(c)):
    if i != c[i][0]:
        ans = 0
        break
    ans *= pow(c[i - 1][1],c[i][1], 998244353)
print(ans%998244353)
