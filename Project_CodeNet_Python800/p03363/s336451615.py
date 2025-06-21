from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
total = [a[0]] * n
cnt = defaultdict(int)
cnt[a[0]] += 1
for i in range(1, n):
    total[i] = total[i - 1] + a[i]
    cnt[total[i]] += 1

ans = 0
for k, v in cnt.items():
    if k == 0:
        ans += v
    ans += v * (v - 1) // 2
#print(total)
print(ans)
