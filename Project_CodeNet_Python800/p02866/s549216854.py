# import bisect
from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    d = list(map(int,ipti().split()))
    d_max = max(d)
    c = Counter(d)

    if d[0] != 0 or c[0] >= 2:
        print(0)
    else:
        ans = 1
        for i in range(d_max):
            if c[i] == 0:
                ans = 0
                break
            else:
                ans *= c[i] ** c[i+1]
        print(ans%998244353)


if __name__ == '__main__':
    main()