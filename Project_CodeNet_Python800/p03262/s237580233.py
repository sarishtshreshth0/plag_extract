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

#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N,X = zz()
x = zz()

distance = [0]*N
for i in range(N):
    distance[i] = abs(x[i] - X)
# print(distance)
ans = distance[0]
for d in distance:
    ans = gcd(ans, d)
    # print(ans)
print(ans)