# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, g = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if n == 1:
        print(abs(a[0]-g))
        return
    
    a.append(g)
    a.sort()
    b = []
    for i in range(1, n+1):
        b.append(a[i]-a[i-1])
    g = b[-1]
    for e in b:
        g = gcd(e, g)
    print(g)
    




        

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
