n=int(input())
r=[list(map(int,input().split())) for i in range(n)]
b=[list(map(int,input().split())) for i in range(n)]
b.sort(key=lambda x:x[0])
cnt=0
r_used=[False]*n
for i in range(n):
  bx,by=b[i][0],b[i][1]
  max_y=-1
  idx=-1
  for j in range(n):
    if r[j][0]<bx and r[j][1]<by and max_y<r[j][1] and not r_used[j]:
      idx=j
      max_y=r[j][1]
  if idx>=0:
    r_used[idx]=True
    cnt+=1
print(cnt)