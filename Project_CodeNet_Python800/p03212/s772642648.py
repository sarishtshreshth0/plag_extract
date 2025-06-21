import sys
sys.setrecursionlimit(10000000)
n=int(input())
tex=['3','5','7']

def dfs(value):
  ans=0
  if value != '' and int(value) > n:
    return 0
  for x in tex:
    if not x in value:
      break
  else:
    ans += 1 
  for x in tex:
    ans += dfs(value+x)
  #print(value,ans)
  return ans

print(dfs(''))