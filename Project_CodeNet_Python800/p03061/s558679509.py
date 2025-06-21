#!/usr/bin/env python3

import sys
from math import gcd
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))


# L[i] = gcd(A[0], A[1], ... , A[i-1])
# R[N-i] = gcd(A[i+1], A[i+2], ..., A[N-1])
L = [0]
R = [0]

for i in range(N):
    L.append(gcd(L[i], A[i]))
    R.append(gcd(R[i], A[N-i-1]))


# M[i] = gcd(L[i], R[N-i
M = [gcd(L[i], R[N-i-1]) for i in range(N)]
print(max(M))

