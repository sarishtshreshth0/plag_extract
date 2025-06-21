import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from collections import *
import math
from bisect import *
import functools
INF = float('inf')
mod = 10**9+7

M, D = map(int, input().split())
ans = 0
for i in range(1, M+1):
    for j in range(2, D+1):
        s, t = j//10, j%10
        if s >= 2 and t >= 2 and i == s * t:
            ans += 1
print(ans)