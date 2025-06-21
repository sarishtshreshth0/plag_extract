n=int(input())

def dfs(s):
  if s!="" and int(s)>n:
    return 0
  
  if len(set(list(s)))<3:
    ret=0
  else:
    ret=1
  
  for i in "753":
    ret+=dfs(s+i)
  
  return ret

print(dfs(""))