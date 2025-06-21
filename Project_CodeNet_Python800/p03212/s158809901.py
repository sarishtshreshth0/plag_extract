n = int(input())

def dfs(k):
  if int(k) > n:
    return 0
  ans = 1 if all(k.count(c) >= 1 for c in '753') else 0
  for c in '753':
    ans += dfs(k+c)
  return ans

print(dfs('0'))