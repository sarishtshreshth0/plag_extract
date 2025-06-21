import numpy as np
n = int(input())
W = np.array(list(map(int, input().split())))
T = np.sum(W)
S = np.cumsum(W)
ans = np.min(np.abs(T - S - S))
print(ans)
