n,a,b = map(int,input().split())
Mod = 10**9+7



def Mod_pow(x, n):
    x = x%Mod
    if n==0:
        return 1
    elif n%2==1:
        return (x*Mod_pow(x,n-1)%Mod)
    else:
        return (Mod_pow(x*x,n/2)%Mod)


def comb(n,r):
    x,y = 1,1
    for i in range(n-r+1,n+1):
        x = x*i%Mod

    for i in range(1,r+1):
        y = y*i%Mod

    #この問題の特徴，フェルマーの小定理よりyで除算することはy^(Mod-2)をかけることと同値
    y = Mod_pow(y,Mod-2)
    return x*y%Mod

ans = (Mod_pow(2,n)-1-comb(n,a)-comb(n,b))
while ans<0:
    ans += Mod

print(ans)