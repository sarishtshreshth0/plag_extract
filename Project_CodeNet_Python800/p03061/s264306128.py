from fractions import gcd
from collections import deque
n = int(input())
a = list(map(int, input().split()))
l = [0]
r = deque([0])
g = []
for i in range(n):
    l.append(gcd(l[i], a[i]))
    r.appendleft(gcd(r[-(i + 1)], a[-(i + 1)]))
r = list(r)

for i in range(n):
    g.append(gcd(l[i], r[i + 1]))
print(max(g))