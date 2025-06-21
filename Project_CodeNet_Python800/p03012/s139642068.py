import numpy as np
n = int(input())
w = np.array([int(i) for i in input().split()])
ans = 10000000
for t in range(1,n):
    s1 = w[:t].sum()
    s2 = w[t:].sum()
    ans = min(ans, np.abs(s1-s2))
print(ans)
