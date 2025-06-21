import math
n=int(input())
ans = 10**10
for a in range(1,int(math.sqrt(n))+1):
  if n%a:
    continue
  b = n//a
  ans = len(str(b))
print(ans)