import math

n = int(input())
a = list(map(int,input().split()))

ar = a[::-1]
l = [0]
r = []

tmp1 = 0
tmp2 = 0
for i in range(n-1):
    tmp1 = math.gcd(tmp1, a[i])
    l.append(tmp1)
    tmp2 = math.gcd(tmp2, ar[i])
    r.append(tmp2)

r.reverse()
r.append(0)
ans = 1
for i in range(n):
    ans = max(ans, math.gcd(l[i], r[i]))
print(ans)