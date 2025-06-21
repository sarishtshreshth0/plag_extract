# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b
# まず、本当に木を構築するモノではないだろう
from collections import Counter
n = int(input())
nums = [int(i) for i in input().split()]
mod = 998244353
MAX = max(nums)

c = Counter(nums)
if nums[0] != 0 or nums.count(0) != 1:
    ans = 0
else:
    ans = 1
    for i in range(1, MAX + 1):
        ans = ans * pow(c.get(i - 1, 0), c.get(i, 0), mod) % mod
    ans %= mod
print(ans)