# -*- coding: utf-8 -*-
import math

N, K = map(int, input().split())

n = int(math.sqrt(N)) + 1

for i in range(n, -1, -1):
  if K ** i <= N:
    print(i+1)
    exit()