N = int(input())

def dfs(n):
  if int(n) > N:
    return 0
  if ('3' in n) and ('5' in n) and ('7' in n):
    ret = 1
  else:
    ret = 0
  for c in '357':
    ret += dfs(n+c)
  return ret

print(dfs('0'))