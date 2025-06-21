N=int(input())
a=[[] for i in range(N)]
for i in range(N):
  a1,b1=map(int,input().split())
  a[i].extend([a1,b1])
a.sort()
c=[]
d=[]
for i in range(N):
  c1,d1=map(int,input().split())
  c.append(c1)
  d.append(d1)
count=0
flag=[0 for i in range(N)]
for i in range(N):
  y=a[N-1-i][1]
  tmp=-1
  minb=max(d)
  fl=False
  for j in range(N):
    if(c[j]>a[N-1-i][0]):
      if(d[j]<=minb and d[j]>y and flag[j]==0):
        fl=True
        tmp=j
        minb=d[j]
  if fl:
    flag[tmp]=1
    count+=1
print(count)