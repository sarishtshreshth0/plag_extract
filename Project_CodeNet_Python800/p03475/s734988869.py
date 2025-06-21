import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N = int(input())

C = [0] * N
S = [0] * N
F = [0] * N

for i in range(N - 1):
    c, s, f = map(int, input().split())
    C[i] = c
    S[i] = s
    F[i] = f

for i in range(N - 1):
    arrive = S[i] + C[i]
    for j in range(i + 1, N - 1):
        if arrive < S[j]:
            arrive = S[j] + C[j]
        elif arrive % F[j] == 0:
            arrive += C[j]
        else:
            w = F[j] - (arrive % F[j])
            arrive += C[j] + w
    print(arrive)
print(0)

