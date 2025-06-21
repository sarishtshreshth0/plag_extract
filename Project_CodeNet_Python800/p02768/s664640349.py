def per(n, r, mod=10**9+7):  # 順列数
    per = 1
    for i in range(r):
        per = per*(n-i) % mod
    return per
 
 
def com(n, r, mod=10**9+7):  # 組み合わせ数
    bunshi = per(n, r, mod)
    bunbo = 1
    for i in range(1, r+1):
        bunbo = bunbo*i % mod
    return bunshi*pow(bunbo, -1, mod)%mod
 
 
n, a, b = map(int, input().split())
 
ans = pow(2,n,10**9+7)
 
print((ans-com(n,a)-com(n,b)-1)%(10**9+7))