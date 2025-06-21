# -*- coding: utf-8 -*-

N, K = map(int, input().split())

cnt = 1
val = N
while val >= K:
    val = val / K
    cnt += 1

print(cnt)