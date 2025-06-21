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
num = ['7', '5', '3']
stack = [('', 0)]
ans = 0
check = defaultdict(lambda:True)
while stack:
    m, l = stack.pop()
    for x in num:
        if x not in m:
            break
    else:
        ans += 1
    for x in num:
        if 10 * l + int(x) <= n:
            if check[10*l + int(x)]:
                stack.append((m + x, 10 * l + int(x)))
                check[10*l + int(x)] = False
print(ans)