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
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    s = list(input())
    t = list(input())

    sl = len(s)
    tl = len(t)

    dp = [[0 for _ in range(tl + 1)] for __ in range(sl + 1)]

    for i in range(sl):
        for j in range(tl):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    ans = ""
    x = sl
    y = tl
    while x > 0 and y > 0:
        if s[x - 1] == t[y - 1]:
            ans = s[x - 1] + ans
            x -= 1
            y -= 1
        elif dp[x][y] == dp[x][y - 1]:
            y -= 1
        elif dp[x][y] == dp[x - 1][y]:
            x -= 1

    print(ans)


if __name__ == '__main__':
    main()
