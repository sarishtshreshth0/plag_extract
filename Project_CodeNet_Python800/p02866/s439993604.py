from collections import Counter

MOD = 998244353
N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
    exit()

C = sorted(Counter(D).most_common(), key=lambda x: x[0])

if C[0][1] > 1:
    print(0)
    exit()

ans = 1
for i in range(1, len(C)):
    if C[i][0] - C[i-1][0] > 1:
        print(0)
        exit()
    ans *= C[i - 1][1] ** C[i][1]

print(ans % MOD)
