from collections import Counter

n = int(input())
d = list(map(int, input().split()))
mod = 998244353
if d[0] != 0 or 0 in d[1:]:
    print(0)
else:
    c = Counter(d)
    ans = 1
    for i in range(1, len(c)):
        ans *= c[i-1] ** c[i]
        ans %= mod
    print(ans % mod)
