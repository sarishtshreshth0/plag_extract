#!/usr/bin/env python3

import math

N, X = map(int, input().split())
A = sorted(list(map(int, input().split()))+[X])
B = []

for i in range(len(A)-1):
    B.append(A[i+1] - A[i])

g = B[0]

for b in B[1:]:
    g = math.gcd(b, g)

print(g)

