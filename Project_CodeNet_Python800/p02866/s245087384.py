from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))

depth = defaultdict(int)
for d in D:
    depth[d] += 1

# つながらない
if D[0] != 0 or depth[0] != 1:
    print(0)
    exit()

mod = 998244353
ans = 1
for d in range(1, max(D) + 1):
    ans *= pow(depth[d - 1], depth[d], mod)
    ans %= mod
print(ans)