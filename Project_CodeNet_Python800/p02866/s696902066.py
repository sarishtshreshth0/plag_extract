n = int(input())
D = tuple(map(int, input().split()))
maxd = max(D)
mod = 998244353
cd = [0] * (maxd+1)
for d in D:
    cd[d] += 1

pre_nodes = cd[0]
if pre_nodes != 1 or D[0] != 0:
    print(0)
    exit(0)

ans = 1
for i in range(1, maxd+1):
    nodes = cd[i]
    ans *= pow(pre_nodes, nodes, mod)
    ans %= mod
    pre_nodes = nodes
else:
    print(ans)
