from subprocess import*
call(('pypy3','-c',"""
s=input()
t=input()
a=len(s)
b=len(t)
dp=[[0]*(b+1) for i in range(a+1)]
for i in range(a):
  for j in range(b):
    if s[i]==t[j]:
      dp[i+1][j+1]=dp[i][j]+1
    else:
      dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
res=''
while a!=0 and b!=0:
  if dp[a][b]==dp[a-1][b]:
    a-=1
  elif dp[a][b]==dp[a][b-1]:
    b-=1
  else:
    a-=1
    b-=1
    res=s[a]+res
print(res)
"""))
"""
from subprocess import*
import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
from math import *
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
import copy
import time
# import numpy as np
starttime = time.time()
# import numpy as np
mod = int(pow(10, 9) + 7)
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]

try:
    # sys.setrecursionlimit(int(pow(10,6)))
    # sys.stdin = open("input.txt", "r")
    # sys.stdout = open("../output.txt", "w")
except:
    pass

"""
