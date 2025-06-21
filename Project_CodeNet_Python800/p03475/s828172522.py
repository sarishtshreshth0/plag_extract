# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


def solve():
    # n, m = [int(x) for x in input().split()]  
    n = int(input())
    a = []
    for _ in range(n-1):
        a.append([int(x) for x in input().split()])

    for i in range(n-1):
        c, s, f = a[i]

        cur = s + c
        for j in range(i+1, n-1):
            c, s, f = a[j]
            if s > cur:
                cur = s
            else:
                x = (cur + f - 1) // f
                cur = x * f

            cur += c
            
        print(cur)

    print(0)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
a b a
d c d
a b a
"""
