n,a,b = map(int,input().split())
#組み合わせ(数が大きいとき)(10**9+7で割ったもの)
q = 10**9+7
def comb(a, b):
    c = 1
    for i in range(b):
        c *= a - i
        c %= q
    d = 1
    for i in range(b):
        d *= i + 1
        d %= q
    return c*pow(d, q-2, q)
p = pow(2,n,q)-1-comb(n,a)-comb(n,b)
print(p%(10**9+7))