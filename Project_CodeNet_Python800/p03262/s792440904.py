import functools
import math

n, x_init = map(int, input().split())
x = list(map(int, input().split()))
x.append(x_init)
x.sort()

dist_next = []
for i in range(n):
    dist_next.append(x[i + 1] - x[i])

ans = functools.reduce(math.gcd, dist_next)
print(ans)
