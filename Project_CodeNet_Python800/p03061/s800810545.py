"""
累積GCD
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

from math import gcd

L = [0] * n
R = [0] * n

for i in range(n-1):
    L[i+1] = gcd(L[i], A[i])
for i in range(n-1, 0, -1):
    R[i-1] = gcd(R[i], A[i])

ans = 0
for i in range(n):
    ans = max(ans, gcd(L[i], R[i]))

print(ans)
