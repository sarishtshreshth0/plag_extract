def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

N = getN()
dist = [[] for i in range(N)]
edge = {}
for i in range(N - 1):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)
    # queryの何番目のエッジか
    edge[(a - 1, b - 1)] = i
    edge[(b - 1, a - 1)] = i

ignore = [-1] * N
ignore[0] = 0
ans = [0] * (N - 1)

pos = deque([0])
while len(pos) > 0:
    u = pos.popleft()
    j = 1
    for i in dist[u]:
        if ignore[i] < 0:
            if j == ignore[u]:
                j += 1
            ignore[i] = j
            ans[edge[(i, u)]] = j
            pos.append(i)
            j += 1
print(max(ans))
for i in ans:
    print(i)