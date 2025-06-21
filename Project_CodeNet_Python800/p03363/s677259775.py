import itertools
import collections
n = int(input())
aaa = list(map(int, input().split()))
cnt = [0] * n
cnt[0] = aaa[0]
for i in range(1, n):
    cnt[i] = cnt[i - 1] + aaa[i]
cnt = [0] + cnt
num_cnt = collections.Counter(cnt)
ans = 0
for num in num_cnt.most_common():
    if num[1] != 1:
        ans += num[1] * (num[1] - 1) // 2
print(ans)