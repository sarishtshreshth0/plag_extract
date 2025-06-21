# -*- coding: utf-8 -*-
import sys
# from collections import defaultdict, deque
# from math import sqrt, gcd, factorial, tan, pi, sin, cos
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]

MOD = 998244353

def solve():
    n = int(input())
    d = [int(x) for x in input().split()]
    f = [0] * n
    for e in d:
        f[e] += 1
    
    ok = f[0] == 1 and d[0] == 0
    z = 0
    ans = 1
    for i in range(1, n):
        if (f[i] == 0): z = 1
        if (z and f[i]): ok = 0
        ans *= pow(f[i-1], f[i], MOD)
        ans %= MOD
    print(ans * ok)




t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()



"""
1 -> (1, 2) -> (2 ** 3, 3) -> (3, 1)

"""

