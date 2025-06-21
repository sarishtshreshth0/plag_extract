from math import gcd
n, x = map(int, input().split())
x = list(map(lambda xi: abs(int(xi) - x), input().split()))
g = x[0]
for xi in x:
    g = gcd(g, xi)
print(g)
