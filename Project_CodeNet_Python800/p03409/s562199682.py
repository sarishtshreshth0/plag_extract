n = int(input())
AB = [list(map(int,input().split())) for _ in range(n)]
CD = [list(map(int,input().split())) for _ in range(n)]

que = [[] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if AB[i][0] < CD[j][0] and AB[i][1] < CD[j][1]:
      que[j].append(i)

def dfs(i,v):
  
  for a in que[i]:
    if a in v:
      continue
    v.add(a)
    if ab[a] == -1 or dfs(ab[a], v):
      ab[a] = i
      return True
  return False
      
v = [set() for _ in range(n)]   
ab = [-1]*n

print(sum(dfs(i, set()) for i in range(n))) 