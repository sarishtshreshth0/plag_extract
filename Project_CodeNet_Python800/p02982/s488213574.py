import math
import numpy as np
n, d = map(int, input().split())
X = np.array([list(map(int, input().split())) for _ in range(n)])
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = math.sqrt(np.sum((X[i] - X[j]) ** 2))
        if dis == int(dis):
            ans += 1
print(ans)
