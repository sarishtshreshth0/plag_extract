n = int(input())
a = list(map(int, input().split()))

nums = [0]*(max(a)+1)
for i in a: nums[i] += 1
ans = sum(nums[:3])
t = sum(nums[:3])
for i in range(len(nums)-3):
  t = t + nums[i+3] - nums[i]
  if ans < t: ans = t
print(ans)