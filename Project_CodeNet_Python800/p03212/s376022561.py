N = int(input())
def dfs(s):
  if int(s)>N:
    return 0
  if all(s.count(i)>0 for i in "357"):
    c = 1
  else:
    c = 0
  for i in "357":
    c += dfs(s+i)
  return(c)
print(dfs("0"))