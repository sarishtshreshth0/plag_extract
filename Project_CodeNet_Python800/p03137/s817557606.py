import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()

    ans = 0
    if n<m:
        L = []
        for i in range(m-1):
            L.append(l[i+1] - l[i])
        L.sort()
        for i in range(m-n):
            ans += L[i]
    print(ans)

if __name__=="__main__":
    main(
    )
