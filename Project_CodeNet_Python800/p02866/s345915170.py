mod = 998244353 
n= int(input())
d= list(map(int,input().split()))
if (d[0]!=0) or (0 in d[1:]):
    print(0)
    exit(0)
md=max(d)
def pf(a,n,p):
  bi=str(format(n,"b"))
  res=1
  for i in range(len(bi)):
    res=(res*res) %p
    if bi[i]=="1":
      res=(res*a) %p
  return res
tl=[0]*md
for c in d[1:]:tl[c-1]+=1
if 0 in tl:
    print(0)
    exit(0)
ans=1
for i in range(md-1):ans=(ans%mod*pf(tl[i],tl[i+1],mod))%mod
print(ans)