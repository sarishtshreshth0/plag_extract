from collections import Counter
N = int(input())
D = list(map(int, input().split()))
MOD = 998244353
ans = 1
dep = Counter(D)
if dep[0] != 1 or D[0] != 0:
    print(0)
    exit(0)
if max(D) == 0:
    pass
else:
    for i in range(1, max(D) + 1):
        if dep[i] == 0:
            print(0)
            exit(0)
        else:
            ans *= dep[i-1] ** dep[i]
            ans %= MOD
print(ans)