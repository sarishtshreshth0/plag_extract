from collections import defaultdict
n = int(input())
d = list(map(int, input().split()))
cnt = defaultdict(int)
if d[0] != 0:
    print(0)
else:
    ans = 1
    for i in range(n):
        cnt[d[i]] += 1
    for i in range(1, n):
        ans = (ans * cnt[d[i] - 1] % 998244353)

    print(ans)