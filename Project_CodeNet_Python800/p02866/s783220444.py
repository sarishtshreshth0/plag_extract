from collections import Counter

n = int(input())
d = list(map(int, input().split()))
mod = 998244353
cnt = Counter(d)

if d[0] != 0 or cnt[0] != 1:
    print(0)
    exit()

ans = 1
for i in range(len(cnt)+1):
    ans *= pow(cnt[i], cnt[i+1], mod)
    ans %= mod
print(ans)
