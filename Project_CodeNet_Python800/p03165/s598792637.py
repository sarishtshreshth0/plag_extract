import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
#from decimal import *
		
s = input()
t = input()
 
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)):
	for j in range(len(t)):
		if s[i] == t[j]:
			dp[i+1][j+1] = dp[i][j] + 1
		else:
			dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            
y = len(s)
x = len(t)
ans = ""
while 1:
	#print(y, x, ans)
	if x*y == 0:
		break
	elif s[y-1] == t[x-1]:
		ans += s[y-1]
		x -= 1
		y -= 1
	else:
		if dp[y][x] == dp[y-1][x]:
			y -= 1
		elif dp[y][x] == dp[y][x-1]:
			x -= 1
            
print(ans[::-1])