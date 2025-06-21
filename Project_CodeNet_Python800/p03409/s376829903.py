# Ford-Fulkerson algorithm
class FordFulkerson:
  def __init__(self, N):
    self.N = N
    self.edge = [[] for i in range(N)]

  def add_edge(self, fr, to, cap):
    forward = [to, cap, None]
    forward[2] = backward = [fr, 0, forward]
    self.edge[fr].append(forward)
    self.edge[to].append(backward)

  def add_multi_edge(self, v1, v2, cap1, cap2):
    edge1 = [v2, cap1, None]
    edge1[2] = edge2 = [v1, cap2, edge1]
    self.edge[v1].append(edge1)
    self.edge[v2].append(edge2)

  def dfs(self, v, t, f):
    if v == t:
      return f
    used = self.used
    used[v] = 1
    for e in self.edge[v]:
      w, cap, rev = e
      if cap and not used[w]:
        d = self.dfs(w, t, min(f, cap))
        if d:
          e[1] -= d
          rev[1] += d
          return d
    return 0

  def flow(self, s, t):
    flow = 0
    f = INF = 10**9 + 7
    N = self.N
    while f:
      self.used = [0]*N
      f = self.dfs(s, t, INF)
      flow += f
    return flow

import sys
readline = sys.stdin.readline

N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
ff = FordFulkerson(2*N+2)
for v in range(1,N+1):
  ff.add_edge(0,v,1)
for v in range(N):
  ff.add_edge(1+N+v,2*N+1,1)
for u,(a,b) in enumerate(R):
  for v,(c,d) in enumerate(B):
    if a<c and b<d:
      ff.add_edge(1+u,1+N+v,1)
ans = ff.flow(0,2*N+1)
print(ans)