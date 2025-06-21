from collections import Counter
MOD = 998244353

N = int(input())

D = list(map(int, input().split()))

if D[0] > 0:
    print(0)
    exit()

c = Counter(D)
if c[0] > 1:
    print(0)
    exit()

ans = 1
for i in range(1, max(c)+1):
    if not c[i]:
        print(0)
        exit()
    
    ans *= pow(c[i-1], c[i], MOD) % MOD

print(ans%MOD)