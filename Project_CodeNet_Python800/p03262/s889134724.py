import math

n, x = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
  b.append(abs(x-a[i]))
ans = b[0]
for j in range(1, n):
  ans = math.gcd(ans, b[j])
print(ans)