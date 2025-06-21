# import numpy as np
import sys, math, heapq
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")

N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    c, s, f = CSF[i]
    time = s + c
    for csfj in CSF[i + 1 :]:
        c, s, f = csfj
        if time < s:
            time = s
        else:
            time = f * ((time + f - 1) // f)
        time += c
    print(time)

print(0)