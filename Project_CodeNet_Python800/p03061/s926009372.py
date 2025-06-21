import math
n = int(input())
a = list(map(int,input().split()))
r ,l = [0] * (n),[0] * (n)
l[0] = 0
r[n-1] = 0
for i in range(1,n):
    l[i] = math.gcd(l[i-1],a[i-1])
    r[n-i-1] = math.gcd(r[n-i],a[n-i])
m = [0] * n
for i in range(n):
    m[i] = math.gcd(l[i],r[i])
print(max(m))
