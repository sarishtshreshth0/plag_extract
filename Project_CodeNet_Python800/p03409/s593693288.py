n=int(input())
r=[tuple(map(int,input().split())) for i in range(n)]
b=[tuple(map(int,input().split())) for i in range(n)]
r.sort(key=lambda x: x[1],reverse=True)
b.sort(key=lambda x: x[0])
selected=[0]*n

ans=0
for i in range(n):
  bx,by=b[i]
  j=0
  while j<n:
    rx,ry=r[j]
    if bx>rx and by>ry and selected[j]==0:
      ans+=1
      selected[j]=1
      break
    j+=1
print(ans)

