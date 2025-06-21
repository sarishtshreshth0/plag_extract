N = int(input())
def dfs(x):
  ret = 0
  if int(x)>N:
    return 0
  if all(x.count(i)>0 for i in "753"):
    ret += 1
  for i in "753":
    ret += dfs(x+i)
  return ret
print(dfs("0"))