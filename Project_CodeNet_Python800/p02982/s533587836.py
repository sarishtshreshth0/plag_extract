# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def d(a, b):
    ans = 0
    n = len(a)
    for i in range(n):
        ans += (a[i] - b[i]) ** 2
    return int(ans**0.5) == ans**0.5

def solve():
    n, _ = [int(x) for x in input().split()]
    ans = 0
    points = []
    for _ in range(n):
        arr = [int(x) for x in input().split()]   
        points.append(arr)
    for i in range(n):
        for j in range(i+1, n):
            ans += d(points[i], points[j])
    print(ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()




"""

4
1 2
2 4
1 3
3
2 2 4
4 5 6

6
1 2
2 3
3 4
4 5
4 6
3
3 5 6
2 17 31 5 11

"""



