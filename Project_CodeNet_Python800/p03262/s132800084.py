import math

n, x = map(int, input().split())
lis = list(map(int, input().split()))

nlis = []

for i in range(n):
    nlis.append(abs(lis[i]- x))

ans = nlis[0]

for j in range(1, n):
    ans = math.gcd(ans, nlis[j])

print(ans)