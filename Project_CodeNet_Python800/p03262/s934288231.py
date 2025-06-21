N,X = map(int,input().split())
City = list(map(int,input().split()))

for i in range(N):
  City[i] = abs(X-City[i])
import math
d = City[0]
for i in range(1,N):
  d = math.gcd(d,City[i])
print(d)