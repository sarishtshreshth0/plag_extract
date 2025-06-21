# https://atcoder.jp/contests/agc023/tasks/agc023_a

from collections import Counter
n = int(input())
nums = [0] + [int(i) for i in input().split()]

def nC2(n):
    return n * (n - 1) // 2

for i in range(n):
    nums[i + 1] += nums[i]
c = Counter(nums)
ans = 0
for v in c.values():
    ans += nC2(v)
print(ans)
