import sys
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
import collections
from collections import deque 

input = sys.stdin.readline

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

s = input()
t = input()
_debug(s)
dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]

for i in range(1, len(s)+1):
    ch = s[i-1]
    for j in range(1, len(t)+1):
        if ch == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 文字列作成
length = dp[len(s)][len(t)]
_debug(length)

i = len(s) - 1
j = len(t) - 1
ans = [""] * length
_debug(ans)
while length > 0:
    if s[i] == t[j]:
        ans[length-1] = s[i]
        i -= 1
        j -= 1
        length -= 1
    elif dp[i+1][j+1] == dp[i+1][j]:
        j -= 1
    else:
        i -= 1
print("".join(ans))

