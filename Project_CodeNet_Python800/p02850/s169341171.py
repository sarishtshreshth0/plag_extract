n = int(input())
g = [[] for i in range(n+1)]
d = {}
l = [-1] * (n-1)
max_idx = 0
for i in range(n-1):
  u,v = map(int, input().split())
  d[(u,v)] = i
  d[(v,u)] = i
  g[u].append((u,v))
  g[v].append((v,u))
  if len(g[max_idx]) < len(g[u]):
    max_idx = u
  if len(g[max_idx]) < len(g[v]):
    max_idx = v
m = len(g[max_idx])
stack = []
count = m
while len(g[1]) > 0:
  u2, v2 = g[1].pop()
  l[d[(u2, v2)]] = count
  count -= 1
  stack.append((u2, v2))

while len(stack) > 0:
  u, v = stack.pop()
  #print(u,v)
  if len(g[v]) > 0:
    count = m
    while len(g[v]) > 0:
      u2, v2 = g[v].pop()
      if count == l[d[(u, v)]]:
        count -= 1
      if l[d[(u2, v2)]] == -1:
        l[d[(u2, v2)]] = count
        count -= 1
        stack.append((u2, v2))
print(m)
for i in range(n-1):
  print(l[i])
  
