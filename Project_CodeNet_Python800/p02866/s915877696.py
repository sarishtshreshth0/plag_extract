from collections import Counter
n, *d = map(int, open(0).read().split())
MOD = 998244353
c = Counter(d)
if d[0] != 0 or c[0] != 1:
    ans = 0
else:
    ans = 1
    for i in range(1, max(d)+1):
        ans *= pow(c[i-1], c[i]) % MOD
print(ans % MOD)