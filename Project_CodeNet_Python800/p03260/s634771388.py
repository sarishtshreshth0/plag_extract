a, b = map(int, input().split())
nums = []

for i in range(3):
    i = i + 1
    ans = a * b * i
    if ans % 2 == 0:
        nums.append('No')
    else:
        nums.append('Yes')

if nums.count('Yes'):
    print('Yes')
else:
    print('No')