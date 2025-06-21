def print0():
    print(0)
    exit()

n = int(input())
d = list(map(int, input().split()))
mod = 998244353
ans = 1
maxd = max(d)
numcnt = [0] * (maxd + 1)
for i in d:
    numcnt[i] += 1
if not d[0] == 0 or not numcnt[0] == 1:
    print0()
for i in range(1, maxd + 1):
    if numcnt[i] == 0:
        print0()
    ans *= pow(numcnt[i - 1], numcnt[i], mod)
    ans %= mod
print(ans)