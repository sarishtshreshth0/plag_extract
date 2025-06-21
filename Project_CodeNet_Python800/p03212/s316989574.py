n=int(input())

lim_keta=len(str(n))

def dfs(keta,num):
  if int(num)<=n and len(set(num))==3:
    global cnt
    cnt+=1

  if keta==lim_keta:
    return

  for i in '753':
    dfs(keta+1,num+i)

cnt=0
for i in '753':
  dfs(1,i)

print(cnt)