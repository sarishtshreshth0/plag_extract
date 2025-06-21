
from collections import Counter

N = int(input())
X = list(map(int, input().split()))

MOD = 998244353
ctr = Counter(X)

if X[0] == 0 and ctr[0] == 1:
    ans = 1
    for i in range(1, max(X) + 1):
        ans *= pow(ctr[i - 1], ctr[i], MOD)
        ans %= MOD
    print(ans)
else:
    print(0)
