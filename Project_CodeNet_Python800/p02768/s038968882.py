mod = 10**9 + 7
n, a, b = map(int, input().split())
res = pow(2, n, mod)-1

c1 = 1
for i in range(n-a+1, n+1):
    c1 *= i
    c1 %= mod

for i in range(1, a+1):
    c1 *= pow(i, mod-2, mod)
    c1 %= mod
    
c2 = 1
for i in range(n-b+1, n+1):
    c2 *= i
    c2 %= mod

for i in range(1, b+1):
    c2 *= pow(i, mod-2, mod)
    c2 %= mod
    
res -= (c1+c2)
res %= mod
print(res)