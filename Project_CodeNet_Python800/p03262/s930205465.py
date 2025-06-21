from math import gcd
n,x = map(int, input().split())
l = sorted([x]+list(map(int, input().split())))

nums = [0]*n
for i in range(n): nums[i] = l[i+1] - l[i]

ans = nums[0]
for i in range(1,n):
  ans = gcd(ans,nums[i])
print(ans)