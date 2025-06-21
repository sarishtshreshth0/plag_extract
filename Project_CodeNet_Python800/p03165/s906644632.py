#!/usr/bin/env python
import sys
import re
"""
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)
"""

def solve(S, T):
    L1 = len(S)
    L2 = len(T)
    dp = [[0]*(L2+1) for i in range(L1+1)]

    for i in range(L1-1, -1, -1):
        for j in range(L2-1, -1, -1):
            r = max(dp[i+1][j], dp[i][j+1])
            if S[i] == T[j]:
                r = max(r, dp[i+1][j+1] + 1)
            dp[i][j] = r

    # dp[0][0] が長さの解

    # ここからは復元処理
    res = []
    i = 0; j = 0
    while i < L1 and j < L2:
        if S[i] == T[j]:
            res.append(S[i])
            i += 1; j += 1
        elif dp[i][j] == dp[i+1][j]:
            i += 1
        elif dp[i][j] == dp[i][j+1]:
            j += 1
    return "".join(res)

def main():
    input = sys.stdin.readline
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())
    #ps = list(map(int, input().split()))

    S = input().strip()
    T = input().strip()
    lcs = solve(S, T)
    print(lcs)
    """
    s = [ord(c) - 97 for c in input()]
    t = [ord(c) - 97 for c in input()]
    dp = {}
    memo = {}
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i == 0 or j == 0:
                dp[(i, j)] = 0
            else:
                if s[i - 1] == t[j - 1]:
                    dp[(i, j)] = dp[(i - 1, j - 1)] + 1
                    memo[(i, j)] = (i - 1, j - 1)
                else:
                    if dp[(i - 1, j)] < dp[(i, j - 1)]:
                        dp[(i, j)] = dp[(i, j - 1)]
                        memo[(i, j)] = (i, j - 1)
                    else:
                        dp[(i, j)] = dp[(i - 1, j)]
                        memo[(i, j)] = (i - 1, j)
   
    lcs = []
    while dp[i, j] > 0:
        i, j = memo[(i, j)]
        if s[i] == t[j]:
            lcs.insert(0, chr(s[i] + 97))

    print("".join(lcs))
    """


if __name__ == '__main__':
    main()
