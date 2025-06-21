from collections import Counter
import numpy as np
N = int(input())
A = np.array(input().split(), dtype=int)
cum_sum = np.cumsum(A)
res = Counter(cum_sum)
ans = 0
for k, v in res.items():
  if k == 0:
    ans += v + v * (v - 1) // 2 # nC2
  else:
    ans += v * (v - 1) // 2 # nC2
print(ans)