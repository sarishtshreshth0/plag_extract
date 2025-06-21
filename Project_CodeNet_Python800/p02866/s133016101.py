import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce


def input(): return sys.stdin.readline().strip()


def INT(): return int(input())


def MAP(): return map(int, input().split())


def LIST(): return list(map(int, input().split()))


def ZIP(n): return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


def main():
    N = INT()
    D = LIST()
    if D[0] > 0 or D.count(0) > 1:
        print(0)
        exit()

    D.sort()
    ct = [1] * (max(D)+1)
    for i in range(N):
        if D[i] - D[i-1] > 1:
            print(0)
            exit()
        elif D[i] - D[i-1] == 0:
            ct[D[i]] += 1
    ans = 1
    for i in range(1, max(D)+1):
        ans *= pow(ct[i-1], ct[i], 998244353)
        ans %= 998244353

    print(ans)


if __name__ == '__main__':
    main()
