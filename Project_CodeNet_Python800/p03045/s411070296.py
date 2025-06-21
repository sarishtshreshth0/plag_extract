# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# Aでxの根を求める
def find(A,x):
    p = A[x]
    if p == x: return x
    a = find(A,p)
    A[x] = a
    return a
# Aでxとyの属する集合の併合
def union(A, x, y):
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[by] = bx # 根をbxに統一

N, M = lr()
V = [x for x in range(N+1)]
for _ in range(M):
    x, y, z = lr()
    if find(V, x) != find(V, y):
        union(V, x, y)

V = [find(V, x) for x in V]
s = set(V[1:])
answer = len(s)
print(answer)
# 55
