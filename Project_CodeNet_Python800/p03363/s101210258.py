from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dd = defaultdict(int)
total = 0
dd[0] += 1
for num in a:
    total += num
    dd[total] += 1
    
ans = 0
for i, j in dd.items():
    ans += j * (j - 1) // 2
print(ans)