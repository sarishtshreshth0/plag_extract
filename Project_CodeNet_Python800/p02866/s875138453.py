n,*d=map(int,open(0).read().split())
mod=998244353
c=[0]*(max(d)+1)
for i in d:
  c[i]+=1
ans=1
if (not c[0]==1) or (not d[0]==0):
  print(0)
  exit()
for i in range(max(d)):
  ans*=pow(c[i],c[i+1],mod)
  ans%=mod
print(ans)