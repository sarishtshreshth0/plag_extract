from math import gcd

n, x = map(int, input().split())
a = [int(i) for i in input().split()]
b = []
for i in a:
    b.append(abs(x - i))
g = b[0]
for i in b:
    g = gcd(g, i)
print(g)