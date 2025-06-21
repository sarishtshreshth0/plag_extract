import sys
import numpy as np
import collections as cl
import itertools as it
# import more_itertools as mit
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(100000)

n, d = map(int, input().split())
x = []
for _ in range(n):
    x.append(list(map(int, input().split())))
cnt = 0
for i, j in  it.combinations(x, 2):
    di = 0
    for k in range(d):
        di += (i[k]-j[k])**2
    di = di**(1/2)
    if di.is_integer():
        cnt += 1
print(cnt)