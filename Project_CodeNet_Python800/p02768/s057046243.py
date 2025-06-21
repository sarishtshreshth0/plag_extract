n, a, b = map(int, input().split())
mod = 10 ** 9 + 7

#n種類の花を使って、花束を作る組み合わせは2^n-1通り
#pow(x,y,mod) : (x**y) % mod
ans = pow(2, n, mod)-1

#nCa
nCa = 1
#分子:n*(n-1)*...*(n-a+1)
for i in range(n-a+1, n+1):
    nCa *= i
    nCa %= mod
#分母:1/a! = 1/(1*2*...*a) = 1^(p-2)*2^(p-2)*,,,*a^(p-2)
for i in range(1, a+1):
    nCa *= pow(i, mod-2, mod)
    nCa %= mod
    
#nCb
nCb = 1
for i in range(n-b+1, n+1):
    nCb *= i
    nCb %= mod
for i in range(1, b+1):
    nCb *= pow(i, mod-2, mod)
    nCb %= mod

#2^n-1通りからnCaとnCbを引く
ans -= (nCa + nCb)
ans %= mod
print(ans)
