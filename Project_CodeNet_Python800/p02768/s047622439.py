from math import factorial

n,a,b=map(int,input().split())
mod=10**9+7

up=[1]
down=[1]
comb=[1]
for i in range(1,b+1):
    up.append(up[i-1]*(n-i+1)%mod)
    down.append(down[i-1]*i%mod)
    comb.append(up[i]*pow(down[i],mod-2,mod)%mod)

print((pow(2,n,mod)-1-comb[a]-comb[b])%mod)
