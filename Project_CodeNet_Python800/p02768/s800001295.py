n,a,b = map(int, input().split())

def ruizyou(x,r,mod):
    sisuu=r
    kotae=1
    kake=x
    while sisuu:
        if sisuu&1==True:
            kotae*=kake
        sisuu>>=1
        kake**=2
        kake%=mod
        kotae%=mod
    return kotae

def conbi(n,r,mod):
    ue=1
    for i in range(n-r+1,n+1):
        ue*=i
        ue%=mod

    sita=1

    for i in range(1,r+1):
        sita*=i
        sita%=mod

    sita=ruizyou(sita,mod-2,mod)

    return (ue*sita)%mod

mod=10**9+7

ans=ruizyou(2,n,mod)-conbi(n,a,mod)-conbi(n,b,mod)-1
ans%=mod
print(ans)