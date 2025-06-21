import collections

n = int(input())
d = list(map(int, input().split()))

mod = 998244353

if d[0] != 0:
    print(0)
    exit()

m = max(d)

cnt = collections.Counter(d)
if cnt[0] != 1:
    print(0)
    exit()

ans = 1

for i in range(1, m + 1):
    if cnt[i] == 0:
        print(0)
        exit()
    ans *= pow(cnt[i - 1], cnt[i], mod)
    ans %= mod

print(ans)
