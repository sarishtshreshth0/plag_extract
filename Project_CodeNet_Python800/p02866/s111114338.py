from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))

MOD = 998244353

p = defaultdict(int)
for d in D:
    p[d] += 1

if p[0] == 1 and D[0] == 0:
    ans = 1
    for i in range(max(D)):
        ans *= pow(p[i], p[i + 1], MOD)
        ans %= MOD
        if ans == 0:
            break

    print(ans)

else:
    print(0)
