def count(l):
    res = {}
    for d in l:
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    return res

n = int(input())
data = list(map(int, input().split()))
if data[0] != 0:
    print(0)
    exit()
data = count(data)
mod = 998244353
if data[0] != 1:
    print(0)
    exit()
ans = 1
for depth, edges in data.items():
    if depth == 0:
        continue
    if depth - 1 not in data:
        print(0)
        exit()
    ans *= data[depth-1]**edges
    ans %= mod
print(ans%mod)