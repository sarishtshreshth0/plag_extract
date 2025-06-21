import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd, log
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
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

A, B = MAP()
A -= 1
n = len(str(bin(B)))-2
a = [0]*n
b = [0]*n

def cnt_bit(cnt, N):
	for i in range(n):
		p = N//(2**(i+1)) * 2**i
		q = N%(2**(i+1))
		if 2**i <= q:
			p += min(2**i, q-(2**i-1))
		cnt[i] = p

cnt_bit(a, A)
cnt_bit(b, B)

ans = 0
for i in range(n):
	if (b[i]-a[i])%2:
		ans += 2**i

print(ans)