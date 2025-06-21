from math import gcd
n,m = map(int, input().split())
x = list(map(int, input().split()))

x.append(m)
x = sorted(x)
l = [0]*n
for i in range(n): l[i] = x[i+1] - x[i]

ans = l[0]
for i in range(1,n): ans = gcd(ans,l[i])
print(ans)