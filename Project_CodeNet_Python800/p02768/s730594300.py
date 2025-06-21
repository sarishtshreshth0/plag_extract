n,a,b=map(int,input().split())

mod=10**9+7

ans=pow(2,n,mod)-1

na=1
nb=1

ansa=1
ansb=1

for i in range(1,a+1):
  na*=i
  na%=mod
  
for i in range(n,n-a,-1):
  ansa*=i
  ansa%=mod
  
ansa*=pow(na,mod-2,mod)

for i in range(1,b+1):
  nb*=i
  nb%=mod
  
for i in range(n,n-b,-1):
  ansb*=i
  ansb%=mod
  
ansb*=pow(nb,mod-2,mod)

ans-=ansa
ans-=ansb

ans%=mod


print(ans)
