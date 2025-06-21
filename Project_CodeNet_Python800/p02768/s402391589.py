n,a,b=map(int,input().split())
mod=10**9+7

def power_func(a,n,mod):
  bi=str(format(n,"b"))
  res=1
  for i in range(len(bi)):
    res=(res*res)%mod
    if bi[i]=='1':
      res=(res*a)%mod
  return res

def cmb1(x,y,mod):
  l=1
  for g in  range(x+1-y,x+1):
    l*=g
    l%=mod
  for k in range(1,y+1):
    l*=power_func(k,mod-2,mod)
    l%=mod
    
  return l
    
  return ans

ans=power_func(2,n,mod)-1
ans1=cmb1(n,a,mod)
ans2=cmb1(n,b,mod)

print((ans-ans1-ans2)%mod)