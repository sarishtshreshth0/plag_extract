from collections import Counter
N = int(input())
D = list(map(int, input().split()))
MOD = 998244353


if D[0] != 0:
    print(0)
    exit()


if D.count(0) != 1:
    print(0)
    exit()


ans = 1
C = Counter(D)
for k, v in C.items():
    if k == 0:
        continue
    ans *= pow(C[k - 1], v, MOD)
    ans %= MOD

print(ans % MOD)
