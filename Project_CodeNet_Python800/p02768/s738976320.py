n, a, b = map(int, input().split())
mod = 1000000007

def cmb(N, x):
    numerator = 1
    for i in range(N-x+1, N+1):
        numerator = numerator * i % mod
    denominator = 1
    for j in range(1, x+1):
        denominator = denominator * j % mod
    d = pow(denominator, mod-2, mod)
    return numerator * d
 
a = cmb(n, a)
b = cmb(n, b)

total=(pow(2,n)-(1+a+b))%mod

print(total)
