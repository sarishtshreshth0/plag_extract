#!/usr/bin/env python3

import sys
from math import sqrt
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, D = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(N)]


def check_bi(Y, Z):
    sum_ = 0
    for y, z in zip(Y, Z):
       sum_ += (y-z)**2

    for i in range(int(sqrt(sum_))+1):
        if i * i == sum_:
            return True
    return False


count = 0
for i, x in enumerate(X[:len(X)-1]):
    for y in X[i+1:]:
        count += check_bi(x, y)

print(count)

