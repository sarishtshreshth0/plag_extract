N = int(input())
D = list(map(int, input().split()))
DL = [0] * N
mod = 998244353
if D[0] != 0:
    print(0)
    exit()

for d in D:
    DL[d] += 1

if DL[0] != 1:
    print(0)
    exit()

ans = 1
for i in range(1, N):
    if DL[i] == 0:
        if sum(DL[i:]) != 0:
            print(0)
            exit()
        else:
            print(ans%mod)
            exit()

    ans *= pow(DL[i-1], DL[i], mod)
    ans %= mod
print(ans % mod)
