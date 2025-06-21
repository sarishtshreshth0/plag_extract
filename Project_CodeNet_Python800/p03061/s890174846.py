import math
n = int(input())
a = list(map(int,input().split()))
left = [0]*(n+1)
right = [0]*(n+1)

for i in range(n):
  left[i+1] = math.gcd(left[i],a[i])
for i in range(n-1,-1,-1):
  right[i] = math.gcd(right[i+1],a[i])
ans = 0
for i in range(n):
  tmp = math.gcd(left[i],right[i+1])
  ans = max(tmp,ans)
  
print(ans)