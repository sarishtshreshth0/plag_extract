n, x=map(int, input().split())
l=list(map(int, input().split()))
if len(l)==1:
  print(abs(l[0]-x))
  exit()
import math
ans=x-l[0]
for i in range(n-1):
  ans=math.gcd(ans, l[i+1]-l[i])
print(ans)
