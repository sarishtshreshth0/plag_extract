import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n, _ = rm()
li = np.array([np.array(rl()) for _ in range(n)])
cnt = 0
for i in range(n):
  for j in range(i):
    a = sum((li[i] - li[j]) ** 2)**0.5
    if a - a//1 == 0:
      cnt += 1
print(cnt)







