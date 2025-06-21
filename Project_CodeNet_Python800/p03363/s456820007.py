#!/usr/bin/env python3
# input
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(input())
a = list(map(int, input().split()))
acc = [0] * (n + 1)
for i in range(n):
    acc[i + 1] = acc[i] + a[i]
acc.sort()
# 同じ数の個数をi とすると　sum(iC2) が答え
ans = 0
tmp = 0
num = 0
for i in acc:
    if tmp == i:
        num += 1
    else:
        if num > 1:
            ans += num * (num - 1) // 2
        tmp = i
        num = 1
if num > 1:
    ans += num * (num - 1) // 2
print(ans)
