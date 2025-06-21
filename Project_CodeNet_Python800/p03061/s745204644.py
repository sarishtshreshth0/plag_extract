#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
a = LI()
L = [0] * (n+2)
L[0] = a[0]
R = [0] * (n+2)
R[-1] = a[-1]
for i in range(n):
    L[i+1] = math.gcd(a[i], L[i])
    R[-(i+2)] = math.gcd(a[-(i+1)], R[-(i+1)])

ans = 0
for i in range(1, n+1):
    if i - 1 == 0:
        ans = max(ans, R[i+1])
    elif i == n:
        ans = max(ans, L[i-1])
    else:
        ans = max(ans, math.gcd(L[i-1], R[i+1]))
print(ans)