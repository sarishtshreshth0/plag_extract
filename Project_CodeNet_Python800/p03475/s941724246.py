#!/usr/bin/env python3
import sys
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
"""
後ろから順番に漸化式でいけるかと思ったが、それぞれの駅での電車の間隔が一定でないので、むり
O(n**2)で順番に計算する。
"""


n = int(input())
c, s, f = [0] * (n - 1), [0] * (n - 1), [0] * (n - 1)
for i in range(n - 1):
    c[i], s[i], f[i] = map(int, input().split())
ans = [0] * (n - 1)

for i in range(n - 1):
    time = s[i] + c[i]  # 次の役につく時刻
    for j in range(i + 1, n - 1):
        time = max(math.ceil(time / f[j]) * f[j], s[j]) + c[j]
    ans[i] = time
    print(time)
print(0)
