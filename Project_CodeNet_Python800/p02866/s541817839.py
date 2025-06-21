import collections
N  = int (input())
nums = list(map(int,input().split(" ")))
MOD = 998244353
di = collections.defaultdict(lambda :0)
for num in nums:
    di[num] += 1


ans = 1 if nums[0] == 0 else 1
ans = 0 if 0 in nums[1:]  else 1
bottom = min(nums)
top= max(nums)
for d in range(1,top + 1):
    ans *= pow(di[d - 1] ,di[d ],MOD)


print(ans % MOD)