n,*a=map(int,open(0).read().split())
mod=998244353
d={}
for i in a:
  d[i]=d.get(i,0)+1
b=list(d.items())
b.sort()
ans=1
if a[0]!=0 or len(b)!=b[-1][0]+1 or b[0][1]!=1:
    ans=0
for i in range(1,len(b)):
    ans*=b[i-1][1]**b[i][1]
    ans%=mod
print(ans)