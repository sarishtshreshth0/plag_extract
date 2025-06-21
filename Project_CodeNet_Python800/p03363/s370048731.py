import numpy as np
from collections import Counter
N = int(input())
A = np.array(list(map(int, input().split())))
counters = Counter(np.cumsum(A))
ans = 0
for k, v in counters.items():
    ans += v * (v - 1) // 2
    if k == 0:
        ans += v
print(ans)