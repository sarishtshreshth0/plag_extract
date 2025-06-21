n = int(input())

numOfColors = 0
edges = [[] for j in range(n+1)]
ngColor = [-1]*(n+1)
outsI = [[] for j in range(n+1)]
outs = [0]*(n-1)

for i in range(n-1):
  a, b = map(int, input().split())
  edges[a].append(b)
  outsI[a].append(i)

numOfColors = len(edges[1])
for i in range(2, len(edges)):
  numOfColors = max(len(edges[i])+1, numOfColors)

#print(edges)
#print(outsI)

for i in range(len(edges[1])):
  ngColor[edges[1][i]] = i+1
  outs[outsI[1][i]] = i+1
  
queue = []
queue.extend(edges[1])
while queue != []:
  v = queue.pop(0)
  c = 0
  for i in range(len(edges[v])):
    c += 1
    if c == ngColor[v]:
      c += 1
    ngColor[edges[v][i]] = c
    outs[outsI[v][i]] = c
  queue.extend(edges[v])
#print(ngColor)
print(numOfColors)
for out in outs:
  print(out)

