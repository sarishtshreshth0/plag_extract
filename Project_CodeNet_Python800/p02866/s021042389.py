import sys

# import re
# import math
import collections
# import decimal
# import bisect
# import itertools
# import fractions
# import functools
import copy
# import heapq
# import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
MOD2 = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    d = na()

    c = collections.Counter(d)
    lim = max(c)

    flg = False
    if d[0] != 0:
        flg = True

    if c[0] != 1:
        flg = True

    for i in range(lim + 1):
        if i not in c.keys():
            flg = True
            break

    if flg:
        print(0)
        exit(0)

    ans = 1
    for i in range(2, lim + 1):
        ans *= pow(c[i - 1], c[i], MOD2)
        ans %= MOD2

    print(ans)


if __name__ == '__main__':
    main()
