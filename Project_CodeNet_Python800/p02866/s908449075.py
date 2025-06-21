from collections import Counter
mod = 998244353
num_nodes = int(input())
d_ls = list(map(int, input().split()))
d_max = max(d_ls)
c = Counter(d_ls)

if c[0] == 1 and d_ls[0] == 0 and c[1] > 0:
    ans = 1
else:
    ans = 0

for i in range(1,d_max):
    ans *= c[i] ** c[i+1]
    ans %= mod
print(ans)

