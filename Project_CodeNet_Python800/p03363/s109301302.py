import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    def combinations_count(n, r):
        if n > 1:
            return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
        else:
            return 0

    n = ni()
    a = na()

    a.insert(0, 0)

    perm = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        perm[i] = perm[i - 1] + a[i]

    c = collections.Counter(perm)

    ans = 0
    for v in c.values():
        ans += combinations_count(v, 2)

    print(ans)


if __name__ == '__main__':
    main()
