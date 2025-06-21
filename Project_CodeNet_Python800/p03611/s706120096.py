n = int(input())
a = list(map(int,input().strip().split()))

import collections
c = collections.Counter(a)
_max = 0
for i in range(max(a)+1):
  _sum = c[i-1] + c[i] + c[i+1]
  if _max < _sum:
    _max = _sum
print(_max)