# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
from scipy.special import comb
import copy
sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N = z()
C, S, F = [0]*(N-1), [0]*(N-1), [0]*(N-1)
for i in range(N-1):
    c, s, f = zz()
    C[i], S[i], F[i] = c, s, f

ans = [0]*N
ans[N-2] = C[N-2] + S[N-2]
C_sum = [0]*(N-1)
C_sum[N-2] = C[N-2]
for i in reversed(range(0, N-2)):
    C_sum[i] = C_sum[i+1] + C[i]

for i in range(0, N - 1):
    ans[i] = S[i] + C[i]
    for j in range(i+1, N - 1):
        if (ans[i] <= S[j]):
            wait_time = S[j] - ans[i]
        else:
            wait_time = (-ans[i] % F[j])
        ans[i] += (wait_time + C[j])

    # for i in reversed(range(0, N-2)):
    #     if(S[i] + C[i] <= S[i+1]):
    #         print("つける")
    #         ans[i] = S[i] + C[i] + ans[i+1]
    #     else:
    #         print("つけない")
    #         wait_time = F[i+1] - ((S[i] + C[i]) % F[i+1])
    #         print("wait_time", wait_time)
    #         ans[i] = S[i] + C[i] + ans[i+1] + wait_time

    # else:
    #     ans[i] = ans[i+1] + C[i] + F[i]*2

for ans_ in ans:
    print(ans_)
