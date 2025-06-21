#! /usr/bin/env python3

from fractions import gcd
# from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

ans = lambda x : x % 998244353
MOD = 998244353

N = int(input())
D = [int(_) for _ in input().split()]

c = Counter(D)

ans = 1 * (not D[0]) * (c[0] == 1)
for i in range(1, max(c.keys())+1):
    ans *= pow(c[i-1], c[i], MOD)
    ans %= MOD

print(ans)
