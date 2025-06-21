import queue

N = int(input())
ab = []
deg = [0 for i in range(N)]
child = [[] for _ in range(N)]
edge = {}
color = [0 for _ in range(N-1)]
for i in range(N-1):
  tmp = list(map(int, input().split()))
  deg[tmp[0]-1] += 1
  deg[tmp[1]-1] += 1
 
  child[tmp[0]-1].append(tmp[1]-1)
  child[tmp[1]-1].append(tmp[0]-1)
  tmp = [tmp[0]-1, tmp[1]-1]
  edge[tuple(tmp)] = i
  
q = queue.Queue()
q.put([None, 0, None])
used = [0]
# parent, self, color
while not q.empty():
  current = q.get()
  if current[0] is not None:
    cnt = 1
    for c in child[current[1]]:
  #    if c in used:
  #      continue
      used.append(c)
      if cnt == current[2]:
        cnt += 1
      q.put([current[1], c, cnt])
      ind = [current[1], c] if current[1] < c else [c, current[1]]
      
      color[edge[tuple(ind)]] = cnt
      child[c].remove(current[1])
      cnt += 1
  else:
    for i, c in enumerate(child[current[1]]):
      used.append(c)
      q.put([current[1], c, i+1])
      ind = [current[1], c] if current[1] < c else [c, current[1]]
      #print(edge[tuple(ind)], i+1)
      color[edge[tuple(ind)]] = i+1
      child[c].remove(current[1])

print(max(deg))
for c in color:
  print(c)