def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


N, X = map(int, input().split())
x = [int(a) for a in input().split()]

ans = 0
for xx in x:
    ans = gcd(ans, abs(X - xx))

print(ans)