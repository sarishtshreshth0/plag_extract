n,*a=map(int,open(0).read().split())
mod=998244353
b=[0]*n
for i in a:
    b[i]+=1
ans=0
if a[0]==0 and 1==b[0]:
    ans=1
for i,j in zip(b,b[1:]):
    ans=ans*i**j%mod
print(ans)