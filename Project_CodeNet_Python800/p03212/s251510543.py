n=int(input())

lim_keta=len(str(n))

def dfs(keta,num):
  global cnt
  if keta==lim_keta:
    if int(num)<=n and len(set(num))==3:
      cnt+=1
    return
  if len(set(num))==3:
    cnt+=1
  for i in '753':
    dfs(keta+1,num+i)

cnt=0
for i in '753':
  dfs(1,i)

print(cnt)