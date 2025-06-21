from collections import Counter
from scipy.special import comb

n = int(input())
a = list(map(int,input().split()))

sa = [0]
for i in range(n):
  sa.append(sa[i]+a[i])
ans = 0
c = Counter(sa)
for vi in c.values():
  if vi >= 2:
    ans += comb(vi,2,exact=True)
print(ans)