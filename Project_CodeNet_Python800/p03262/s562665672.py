n,s = map(int,input().split())
x = list(map(int,input().split()))

for i in range(n):
  x[i] = abs(x[i] - s)

import math
for i in range(1,n):
  x[i] = math.gcd(x[i],x[i-1])

print(x[n-1])