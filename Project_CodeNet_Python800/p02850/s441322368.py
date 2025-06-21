import sys
input = sys.stdin.readline
from collections import *

def bfs():
    q = deque([(0, -1)])
    visited = [False]*N
    visited[0] = True
    ans = [-1]*(N-1)

    while q:
        v, prev = q.popleft()
        now = 0

        for nv in G[v]:
            if not visited[nv]:
                if now==prev:
                    now += 1

                visited[nv] = True
                ans[idx[(min(v, nv), max(v, nv))]] = now
                q.append((nv, now))
                now += 1

    return ans

N = int(input())
G = [[] for _ in range(N)]
idx = defaultdict(int)

for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    idx[(min(a-1, b-1), max(a-1, b-1))] = i

ans = bfs()
print(max(ans)+1)

for ans_i in ans:
    print(ans_i+1)