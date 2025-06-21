nums = [int (e) for e in input().split()]

lower = min(nums[1], nums[3])
upper = max(nums[0], nums[2])

if lower > upper:
    print(lower - upper)
else:
    print(0)
