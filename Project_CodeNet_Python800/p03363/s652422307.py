import numpy as np
from collections import Counter

n = int(input())
a = np.array(input().split(), np.int64)
S = np.zeros(n + 1, np.int64)
S[1:] = np.cumsum(a)

cnt = Counter(S)
ans = 0
# for x in cnt:
#     ans += cnt[x] * (cnt[x] - 1) // 2
ans = sum(x*(x-1)//2 for x in cnt.values())
print(ans)