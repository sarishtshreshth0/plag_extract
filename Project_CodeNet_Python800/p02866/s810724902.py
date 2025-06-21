n = int(input())
D = list(map(int, input().split()))
MOD = 998244353

cnt = [0] * n
for d in D:
    cnt[d] += 1

if D[0] == 0 and cnt[0] == 1:
    res = 1
else:
    res = 0

for i in range(1, n):
    res *= pow(cnt[i - 1], cnt[i], MOD)
    res %= MOD

print(res)