#!/usr/bin/env python3
import numpy as np

n, d = map(int, input().split())
x = [np.array([*map(int, input().split())]) for _ in range(n)]
c = 0
for i in range(n):
    for j in range(i + 1, n):
        c += np.linalg.norm(x[i] - x[j]).is_integer()
print(c)
