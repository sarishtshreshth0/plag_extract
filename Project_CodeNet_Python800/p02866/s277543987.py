MOD = 998244353
n = int(input())
d = list(map(int, input().split()))
dist_map = [0]*n
for dist in d:
    dist_map[dist] += 1
ans = 1

if d[0] != 0 or dist_map[0] > 1:
    print(0)
    exit()

for i in range(1, n):
    ans *= pow(dist_map[i-1], dist_map[i], MOD)
    ans %= MOD
print(ans)

