# dfs
import collections,sys
sys.setrecursionlimit(10**9)
n,m,k = map(int, input().split())

friend = [[]*(n+1) for _ in range(n+1)]
block = [[]*(n+1) for _ in range(n+1)]
teams = [0]*(n+1)
for _ in range(m):
  a,b = map(int, input().split())
  friend[a].append(b)
  friend[b].append(a)
for _ in range(k):
  c,d = map(int, input().split())
  block[c].append(d)
  block[d].append(c)
  
def dfs(i):
  teams[i] = team
  for j in friend[i]:
    if teams[j] != 0:
      continue
    dfs(j)

team=1
for i in range(1,n+1):
  if teams[i] != 0:
    continue
  dfs(i)
  team+=1

c = collections.Counter(teams)

for i in range(1,n+1):
  temp = c[teams[i]]-len(friend[i])-1
  for j in block[i]:
    if teams[j] == teams[i]:
      temp -= 1
  print(temp, end='')
  if i != n:
    print(" ", end='')