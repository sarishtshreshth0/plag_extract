n, a, b = map(int, input().split())

ans = pow(2,n,10**9+7)

bunshi = 1
bunbo = 1

for i in range(a):
    bunshi = (bunshi * (n-i)) % (10**9+7)
    bunbo = (bunbo * (i+1)) % (10**9+7)

ans = (ans - bunshi*pow(bunbo,-1,10**9+7) - 1) % (10**9+7)

for i in range(a,b):
    bunshi = (bunshi * (n-i)) % (10**9+7)
    bunbo = (bunbo * (i+1)) % (10**9+7)


ans = (ans - bunshi*pow(bunbo,-1,10**9+7)) % (10**9+7)

print(ans)