# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)
def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N, M = zz()
X = zz()
X = sorted(X)
if (M <= N):
    print(0)
    exit()
distance = [0]*(M-1)
for i in range(M-1):
    # print(X[i+1] - X[i])
    distance[i] = X[i+1] - X[i]
distance = sorted(distance, reverse=True)
distance = distance[N-1:]
print(sum(distance))