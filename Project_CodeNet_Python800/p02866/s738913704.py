N = int(input())
D = list(map(int, input().split()))

M = max(D)
cnt = [0 for i in range(M + 1)]

for d in D:
    cnt[d] += 1

if D[0] != 0:
    print(0)
    exit()
if cnt[0] != 1 or 0 in cnt:
    print(0)
    exit()

res = 1
MOD = 998244353
for i in range(2, M + 1):
    res *= cnt[i - 1] ** cnt[i]
    res %= MOD

print(res)
