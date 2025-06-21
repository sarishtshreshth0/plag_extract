import math

N, X = list(map(lambda n:int(n), input().split(" ")))
x = list(map(lambda y:int(y), input().split(" ")))
x.append(X)
x.sort()
d = list(filter(lambda r: r != 0, [abs(x[i + 1] - x[i]) for i in range(len(x) - 1)]))

gcd = d[0]
for i in range(len(d)):
  gcd = math.gcd(d[i], gcd)

print(gcd)
