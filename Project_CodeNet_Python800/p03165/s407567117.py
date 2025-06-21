from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq

s = "0" + input()
t = "1" + input()

n = len(s)
m = len(t)

dp = [[0]*(m) for i in range(n)]

for i in range(n):
    dp[i][0] = 0
for j in range(m):
    dp[0][j] = 0

for i in range(1,n):
    for j in range(1,m):
        if s[i] == t[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ""
i = n-1
j = m-1
len = dp[n-1][m-1]

while len > 0:
    if s[i] == t[j]:
        ans += s[i]
        i -= 1
        j -= 1
        len -= 1
    elif dp[i][j-1] == dp[i][j]:
        j -= 1
    else:
        i -= 1

print(ans[::-1])
