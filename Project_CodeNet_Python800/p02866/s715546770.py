from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))

MOD = 998244353

p = defaultdict(int)
for d in D:
    p[d] += 1

if p[0] == 1 and D[0] == 0:
    ans = 1
    for i in range(N + 1):
        ans *= p[i] ** p[i + 1]
        ans %= MOD

    print(ans % MOD)

else:
    print(0)
