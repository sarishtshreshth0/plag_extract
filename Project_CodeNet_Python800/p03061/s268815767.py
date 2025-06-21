n = int(input())
a = list(map(int, input().split()))

import math
l_gcd = []
r_gcd = []

c = a[0]
for i in a[:-1]:
  c = math.gcd(c, i)
  l_gcd.append(c)
  
c = a[-1]
for j in a[1:][::-1]:
  c = math.gcd(c, j)
  r_gcd.append(c)
  
ans = max(r_gcd[-1], l_gcd[-1])
for r, l in zip(r_gcd[:-1], l_gcd[:-1][::-1]):
  c = math.gcd(r, l)
  ans = max(ans, c)
print(ans)