n = int(input())
a = list(map(int, input().split()))

nums = [0]*(10**5+1)
for i in a: nums[i] += 1

t = sum(nums[:3])
ans = t
for i in range(3,10**5+1):
  t = t - nums[i-3] + nums[i]
  if ans < t: ans = t
print(ans)