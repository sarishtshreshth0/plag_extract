# -*- coding: utf-8 -*-
from sys import stdin
input = stdin.readline
import numpy as np

N = int(input())
W = list(map(int,input().split()))


temp = 1e+9
for i in range(N):
    res = np.array(W[:i]).sum()
    pos = np.array(W[i:]).sum()

    if(abs(res - pos) < temp):
        temp = abs(res - pos)

print(temp)