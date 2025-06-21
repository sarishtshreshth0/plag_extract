import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
ab = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N-1)]
d = {}

for a, b in ab:
  graph[a] += [b]
  graph[b] += [a]

def dfs(u, pre, c):
  color = 0
  for v in graph[u]:
    if v != pre:
      color += 1
      if color == c:
        color += 1
      d[(u, v)] = color
      d[(v, u)] = color
      dfs(v, u, color)

dfs(0, -1, -1)
s = set()
for a, b in ab:
  s.add(d[(a, b)])

print(len(s))
for a, b in ab:
  print(d[(a, b)])
  
