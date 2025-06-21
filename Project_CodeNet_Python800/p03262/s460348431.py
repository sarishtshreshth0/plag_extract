import math  

N, X = [int(x) for x in input().split()]
Coordinates = [int(x) for x in input().split()]

diff = [abs(x - X) for x in Coordinates]

if len(diff) == 1:
  print(min(diff))
else:
  ans = diff[0]
  for i in range(1, len(diff)):
    ans = math.gcd(ans, diff[i])
  print(ans)