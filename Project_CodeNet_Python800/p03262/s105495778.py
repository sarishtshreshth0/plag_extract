from math import gcd
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
m = 0
for i in range(N):
    if m == 0:
        m = x[i+1]-x[i]
    else:
        m = gcd(m, x[i+1]-x[i])
print(m)
