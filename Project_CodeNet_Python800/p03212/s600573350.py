N=int(input())
def dfs(n):
  if N<int(n):
    return 0
  if all(n.count(c)>0 for c in '753'):
    res=1
  else:
    res=0
  for c in '753':
    res+=dfs(n+c)
  return res
print(dfs('0'))