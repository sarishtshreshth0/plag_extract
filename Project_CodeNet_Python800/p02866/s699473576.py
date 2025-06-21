n = int(input())
d = list(map(int, input().split()))
mod = 998244353

a = [0] * n
for d_ in d:
    a[d_] += 1

res = d[0] == 0 and a[0] == 1
pre = 1
for a_ in a:
    res = res * pre ** a_ % mod
    pre = a_

print(res)