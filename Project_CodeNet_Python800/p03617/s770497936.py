#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

Q, H, S, D, N = map(int, read().split())
H = min(Q * 2, H)
S = min(H *2 , S)

if S * 2 < D:
    print(N * S)
else:
    print(N // 2 * D + N % 2 * S)