n = int(input())

nums = []
for i in range(9):
    if i == 0:
        nums_tmp = ['7', '5', '3']
    else:
        nums_tmp_tmp = []
        for num in nums_tmp:
            nums_tmp_tmp.extend([num + d for d in ('7', '5', '3')])
        nums_tmp = nums_tmp_tmp
    nums.extend(nums_tmp)

ans = 0
for num in nums:
    if ('7' in num) and ('5' in num) and ('3' in num) and (int(num) <= n):
        ans += 1
print(ans)
