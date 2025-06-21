#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc133_a

import math

def distance_square(x, y, d):
    z = 0
    for i in range(d):
        z += (x[i] - y[i]) ** 2
    return z

num, dim = map(int, input().strip().split())
points = [list(map(int, input().strip().split())) for _ in range(num)]

res = 0
for i in range(num):
    for j in range(i):
        z = distance_square(points[i], points[j], dim)
        if z == int(math.sqrt(z)) ** 2:
            res += 1

print(res)
