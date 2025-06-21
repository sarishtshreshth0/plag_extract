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
    s = list(input())

    open_cnt = 0
    close_cnt = 0
    for si in s:
        if si == "(":
            open_cnt += 1
        else:
            if open_cnt == 0:
                close_cnt += 1
            else:
                open_cnt -= 1


    for i in range(close_cnt):
        s.insert(0, "(")

    for i in range(open_cnt):
        s.append(")")

    print(*s, sep="")


if __name__ == '__main__':
    main()
