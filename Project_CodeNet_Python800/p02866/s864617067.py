n = int(input())
d = [int(x) for x in input().split()]
mod = 998244353
m = [0]*n

for x in d:
    m[x] += 1
ans = 1

if d[0] != 0 or m[0] > 1:
    print(0)
else:
    for i in range(1, n):
        ans *= pow(m[i-1], m[i], mod)
        ans %= mod
    print(ans)