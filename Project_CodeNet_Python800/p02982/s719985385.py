import sys
import numpy as np
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, _ = rm()
li = np.array([np.array(rl()) for _ in range(n)])
cnt = 0
for i in range(n):
  for j in range(i):
    a = sum((li[i] - li[j]) ** 2)**0.5
    if a - a//1 == 0:
      cnt += 1
print(cnt)







