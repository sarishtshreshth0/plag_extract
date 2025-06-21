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

n = ri()
li = [rr() for _ in range(n)]
if len(set(li)) != n:
  print('No')
  exit()
else:
  for i in range(n-1):
    if li[i][-1] != li[i+1][0]:
      print('No')
      exit()
  else:
    print('Yes')





