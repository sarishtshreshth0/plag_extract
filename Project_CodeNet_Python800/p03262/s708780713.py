import math
N,start = [int(x) for x in input().split()]
_x = [int(y) for y in input().split()]
x = [0 for y in range(N)]
for i in range(N):
    x[i] = abs(_x[i] - start)
g = x[0]
for i in range(N):
    g = math.gcd(g,x[i])
print(g)
ans = 1
