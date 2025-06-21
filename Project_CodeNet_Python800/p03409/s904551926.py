from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math
from fractions import gcd

NN = 202020
MOD = 10**9+7
INF = float("inf")

n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(n)]

used = [False]*n
A.sort()
B.sort()
count = 0
for i in range(len(B)):
    cand = [-1, -1]
    cand_idx = -1
    for j in range(len(A)):
        if A[j][0] < B[i][0]:
            # print(used[j], cand[1], A[j][1])
            if (not used[j]) and (cand[1] < A[j][1] < B[i][1]):
                cand = A[j]
                cand_idx = j
        else:
            break

    if cand_idx != -1:
        count += 1
        used[cand_idx] = True

print(count)
