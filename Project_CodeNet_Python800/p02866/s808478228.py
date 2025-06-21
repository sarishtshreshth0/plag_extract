mod = 998244353
n = int(input())
d = list(map(int, input().split()))
if d[0] != 0:
    print(0)
    exit()
lis = [0] * n
for i in d:
    lis[i] += 1
if lis[0] != 1:
    print(0)
    exit()
ans = 1
for i in range(1, n):
    ans *= pow(lis[i-1], lis[i], mod)
    ans %= mod
print(ans)