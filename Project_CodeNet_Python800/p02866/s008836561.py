n=int(input())
d=list(map(int,input().split()))
r=1 if d[0]==0 else 0
d=d[1:]
d.sort()
c=1
nc=0
j=1
mod=998244353
for i in d:
  if i<j:
    r=0
  elif i==j:
    nc+=1
    r=(r*c)%mod
  elif i==j+1:
    j=i
    c=nc
    nc=1
    r=(r*c)%mod
  else:
    r=0
print(r)