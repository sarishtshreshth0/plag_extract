from collections import Counter
n = int(input())
d = list(map(int, input().split()))
dist = Counter(d)
mod = 998244353
if d[0] != 0 or dist[0] != 1:
    print(0)
    exit()
ans = 1
for i in range(n-1):
    ans = (ans * pow(dist[i], dist[i + 1], mod)) % mod
print(ans)
