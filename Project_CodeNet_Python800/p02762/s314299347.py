n,m,k = map(int, input().split())

g = [[] for i in range(n+1)]
f = [0]*(n+1)
b = []
for i in range(m):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)
  f[u] += 1
  f[v] += 1
for i in range(k):
  b.append(map(int, input().split()))
count = 0
renketu_list = [-1]*(n+1)
renketu_size = [0]
stack = []
for i in range(1, n+1):
  if renketu_list[i] == -1:
    count += 1
    renketu_list[i] = count
    renketu_size.append(1)
    while len(g[i]) > 0:
      stack.append(g[i].pop())
    while len(stack) > 0:
      v=stack.pop()
      if renketu_list[v] == -1:
        renketu_list[v] = count
        renketu_size[count] += 1
        while len(g[v])>0:
          stack.append(g[v].pop())

s = [0] * (n+1)
for i in range(1, n+1):
  s[i] += renketu_size[renketu_list[i]] - f[i] - 1
  
for i in range(k):
  u, v = b[i]
  if renketu_list[u] == renketu_list[v]:
    s[u] -= 1
    s[v] -= 1

print(" ".join(list(map(str, s[1:]))))
  
