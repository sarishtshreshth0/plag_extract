n, a, b = map(int, input().split())
mod = pow(10,9)+7
bunbo = 1
bunshi = 1
ans = pow(2, n, mod)

for i in range(a):
    bunshi = (bunshi*(n-i)) % mod
    bunbo = (bunbo*(i+1)) % mod

ans =(ans-bunshi*pow(bunbo, -1,mod)) % mod

for i in range(a, b):
    bunshi = (bunshi*(n-i)) % mod
    bunbo = (bunbo*(i+1)) % mod

ans = (ans-bunshi*pow(bunbo, -1,mod)) % mod

print(ans-1)