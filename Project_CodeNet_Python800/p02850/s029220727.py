import sys, copy, math, heapq, bisect
from itertools import accumulate
from collections import deque, defaultdict, Counter
input = sys.stdin.readline # 文字列の入力のとき'/n'まで受け取るので注意!!!
sys.setrecursionlimit(500000)

N = int(input())
G = [dict() for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1][b-1] = i
    G[b-1][a-1] = i
ans = [0]*(N-1)
visited = [0]*N
def dfs(i,color):
    visited[i] += 1
    c = 1
    for j in G[i]:
        if visited[j]:
            continue
        if c==color:
            c += 1
        ans[G[i][j]] = c
        dfs(j,c)
        c += 1
dfs(0,0)
print(max(ans))
for i in range(N-1):
    print(ans[i])
