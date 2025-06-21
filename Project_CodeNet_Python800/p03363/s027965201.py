#!/usr/bin/env python
import sys
from collections import Counter
from itertools import permutations, combinations
from fractions import gcd
#from math import gcd
from math import ceil, floor
import bisect
sys.setrecursionlimit(10 ** 6)
inf = float("inf")

def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    a = tuple(map(int, input().split()))

    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + a[i]
    c = Counter(s)

    ans = 0
    for key in c.keys():
        if c[key] > 1:
            ans += c[key]*(c[key]-1) / 2
    print(int(ans))

if __name__ == '__main__':
    main()