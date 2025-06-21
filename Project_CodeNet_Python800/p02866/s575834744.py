n = int(input())
d = list(map(int,input().split()))
MOD = 998244353
dmax = max(d)
dmin = min(d[1:])
cnt = [0] * n
for i, dd in enumerate(d):
    cnt[dd] += 1

if d[0] != 0 or dmin == 0:
    print(0)
    exit()
ans = 1
before = cnt[0]
for i in range(1,dmax+1):
    ans *= pow(before, cnt[i],MOD)
    before = cnt[i]
ans %= MOD
print(ans)
