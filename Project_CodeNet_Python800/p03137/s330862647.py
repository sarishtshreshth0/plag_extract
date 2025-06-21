#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

# list X をソート O(Mlog(M)) する
# 駒を置いて残る目的地 (X_i, ..., X_j) に対して、訪れない区間の長さ最大化する
# 駒２個目以降をおくたびに、訪れないで済む区間が一つ増える
N, M = map(int, readline().split())

if N >= M:
    print(0)
    sys.exit()

X = list(map(int, readline().split()))
X.sort()

L = []
for i in range(M-1):
    L.append(X[i+1] - X[i])

L.sort(reverse=True)

res = X[M-1] - X[0] - sum(L[:N-1])

print(res)





