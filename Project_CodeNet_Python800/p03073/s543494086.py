import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    s = input().rstrip()
    l = len(s)
    a = 0
    ans = 0

    t = 1
    for i in s:
        if t != int(i):
            a += 1
        t = 1-t
    ans = a
    t = 0
    a = 0
    for i in s:
        if t != int(i):
            a += 1
        t = 1-t
    ans = min(a,ans)
    print(ans)

if __name__=="__main__":
    main()
