N = int(input())

def dfs(s):
  # 再帰の基底部
  if len(s) > 0 and int(s) > N:
    return 0
  
  # s自体が七五三数なら+1
  ret = 1 if all(s.count(c) > 0 for c in '753') else 0
  
  return ret + sum((dfs(s+c) for c in '753'))

print(dfs(''))