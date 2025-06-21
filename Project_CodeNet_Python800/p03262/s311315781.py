from math import gcd

N, X = map(int, input().split())
xs = list(map(int, input().split()))

aX = list(map(lambda x: abs(x-X), xs))

ans = aX[0]
for i in range(1, N):
    ans = gcd(ans, aX[i])
print(ans)
