

from collections import Counter
N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
    exit()

MOD = 998244353

c = Counter(D)
if c[0] != 1:
    print(0)
    exit()

key = list(c.keys())
key.sort()

ans = 1
for k in key:
    if k >= 1:
        if k-1 not in c:
            print(0)
            exit()
        else:
            ans *= c[k-1] ** c[k]
            ans %= MOD

print(ans)