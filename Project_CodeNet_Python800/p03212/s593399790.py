n=int(input())

ans="0"
cnt=0
l=["3","5","7"]

def dfs(now):
  global cnt

  if n<int(now):
    return now
  now=str(now)
  if 1<=now.count("3") and 1<=now.count("5") and 1<=now.count("7"):
    cnt+=1

  for i in l:
    a=now+i
    dfs(a)
  
  return cnt
print(dfs(ans))

