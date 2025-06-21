from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

N, a, b = map(int, input().split())

# C,Pを求める前処理
m = 2*10**5+10
mod = 10**9 + 7


fact = [0]*(m+5)
fact_inv = [0]*(m+5)
inv = [0]*(m+5)

fact[0] = fact[1] = 1
fact_inv[0] = fact_inv[1] = 1
inv[1] = 1

for i in range(2,m+5):
    fact[i] = fact[i-1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod


def cmb_large(n,k,mod):
    ans = 1
    for i in range(n, n-k, -1):
        ans = ans * i
        ans = ans % mod
    return ans * fact_inv[k] % mod

print((pow(2,N,mod)-1-cmb_large(N,a,mod)-cmb_large(N,b,mod)) % mod)