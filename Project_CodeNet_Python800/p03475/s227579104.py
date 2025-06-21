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
    n = ni()
    timeschedule = [na() for _ in range(n - 1)]

    for i in range(n):
        time = 0

        for j in range(i, n - 1):
            c, s, f = timeschedule[j]
            if time < s:
                time = s
            if (time - s) % f:
                time += f - ((time - s) % f)
            time += c

        print(time)


if __name__ == '__main__':
    main()
