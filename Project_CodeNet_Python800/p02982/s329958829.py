import numpy as np
from itertools import combinations
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i, j in combinations(X, 2):
    cnt += (sum(dif**2 for dif in np.array(i) - np.array(j))**.5).is_integer()
print(cnt)
