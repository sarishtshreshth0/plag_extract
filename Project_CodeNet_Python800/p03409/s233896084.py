import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N = INT()
ab = [LIST() for _ in range(N)]
cd = [LIST() for _ in range(N)]

check = [0]*N
ab.sort(key = lambda x: (-x[0],-x[1]))
cd.sort(key = lambda x: (x[0], x[1]))

for c, d in cd:
	idx = -1
	tmp = INF
	for i in range(N):
		if check[i] == 0 and ab[i][0] < c and ab[i][1] < d and tmp > d-ab[i][1] :
			tmp = d-ab[i][1]
			idx = i
	if idx != -1:
		check[idx] = 1

print(sum(check))
