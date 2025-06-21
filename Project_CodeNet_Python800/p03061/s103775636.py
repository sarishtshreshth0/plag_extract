from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
from fractions import gcd
import sys
def I(): return int(input())
def Is(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(input())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(10**6)
MOD = 10**9+7
INF = float('inf')


n = I()
A = LI()
# L = list(accumulate(A, gcd))
# R = list(accumulate(reversed(A), gcd))
tmpl = 0
tmpr = 0
L = []
R = []
for i in range(n):
    tmpl = gcd(tmpl, A[i])
    tmpr = gcd(tmpr, A[-1-i])
    L.append(tmpl)
    R.append(tmpr)

R = list(reversed(R))
# print(L)
# print(R)

ans = max(L[n-2], R[1])
for i in range(1, n-1):
    ans = max(ans, gcd(L[i-1], R[i+1]))

print(ans)
