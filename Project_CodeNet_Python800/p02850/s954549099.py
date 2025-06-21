from collections import deque

N = int(input())

dic = {i:[] for i in range(1,N+1)}

rlt = [0]*(N-1)

for i in range(N-1):
  a,b = map(int, input().split())
  dic[a].append((b,i))
  dic[b].append((a,i))
  
h = deque([(1,1)])

while h:
  j = 1
  c = 0
  t = h.popleft()
  for k in dic[t[0]]:
    if k[0] == t[1]:
      c = rlt[k[1]]
      break
  for k in dic[t[0]]:
    if k[0] == t[1]:
      continue
    if c == j:
      j += 1
    rlt[k[1]] = j
    h.append((k[0],t[0]))
    j += 1
    
print(max(rlt))  
for l in rlt:
  print(l)  