import collections
def subarraySum(nums, k):
    count = total = 0
    cache = collections.defaultdict(int)
    cache[0] = 1
    for num in nums:
        total += num
        count += cache[total - k]
        cache[total] += 1
    return count
A = input()
nums = list(map(int,input().split()))
k = 0
print(subarraySum(nums, 0))