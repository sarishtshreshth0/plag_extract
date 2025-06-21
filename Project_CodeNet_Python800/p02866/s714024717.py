mod = 998244353


n = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
    exit()

CNT = [0] * n
for d in D:
    CNT[d] += 1

if CNT[0] >= 2:
    print(0)
    exit()

ans = 1
for i in range(1, n):
    ans *= pow(CNT[i - 1], CNT[i], mod)
    ans %= mod

print(ans)
