import sys
sys.setrecursionlimit(1000000000)
LET=('3','5','7')
n=int(input())

def dfs(s):
  cnt = 0
  if len(s) >0 and int(s) > n:
    return cnt
  if s.count('3') > 0 and s.count('5')>0 and s.count('7')>0:
    cnt += 1
  for l in LET:
    cnt += dfs(s+l)
  return cnt

print(dfs(''))