# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    ans = a[-1] - a[0]
    b = []
    for i in range(m-1):
        b.append(a[i+1] - a[i])
    b.sort(reverse=True)
    for i in range(min(len(b), n-1)):
        ans -= b[i]
    print(ans)
        

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""
