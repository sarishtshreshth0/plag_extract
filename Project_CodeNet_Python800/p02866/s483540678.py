from collections import defaultdict
import sys
input = sys.stdin.buffer.readline


def mod_pow(x, n, mod=10**9 + 7) -> int:
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
            K %= mod
        x *= x
        x %= mod
        n //= 2

    return (K * x) % mod


MOD = 998244353

n = int(input())
D = [int(i) for i in input().strip().split()]

_max = max(D)

counts = defaultdict(int)

if D[0] != 0:
    print(0)
    sys.exit()

for d in D:
    counts[d] += 1

if counts[0] != 1:
    print(0)
    sys.exit()

ans = 1
for i in range(1, _max + 1):
    if i not in counts.keys():
        print(0)
        sys.exit()
    elif i == 1:
        continue
    else:
        x = counts[i - 1]
        k = counts[i]
        ans = (ans * mod_pow(x, k, MOD)) % MOD

print(ans)
