import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
A = list(sorted((map(int, readline().split()))))

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

L = [0] * (N)
R = [0] * (N)
L[0] = A[0]
R[N - 1] = A[N - 1]

for i in range(1, N):
    L[i] = gcd(L[i - 1], A[i])

for i in range(N - 2, -1, -1):
    R[i] = gcd(R[i + 1], A[i])

ans = 0
# print(L)
# print(R)
for i in range(N):
    x = 0
    if i == 0:
        x = R[1]
    elif i == N - 1:
        x = L[N - 2]
    else:
        x = gcd(L[i - 1], R[i + 1])
    ans = max(ans, x)
print(ans)
