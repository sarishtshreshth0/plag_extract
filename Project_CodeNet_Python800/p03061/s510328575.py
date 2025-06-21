import fractions
n = int(input())
a = list(map(int, input().split()))
l = [0]*(n+1)
l[1] = a[0]
r = [0]*(n+1)
r[n-1] = a[n-1]
for i in range(1, n):
  l[i+1] = fractions.gcd(l[i], a[i])
  r[n-1-i] = fractions.gcd(r[n-i], a[n-1-i])

m = 0

for i in range(n):
  m = max(m, fractions.gcd(l[i], r[i+1]))
print(m)
