from collections import defaultdict, Counter

N = int(input())
D = list(map(int, input().split()))
c = Counter(D)
M = max(c.keys())

if D[0] != 0 or c[0] != 1:
    print(0)
    exit()

mod = 998244353
depth = 1
ans = 1
while depth <= M:
    ans *= pow(c[depth - 1], c[depth], mod)
    ans %= mod
    depth += 1
print(ans)