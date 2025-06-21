from collections import Counter
MOD = 998244353
n = int(input())
D = list(map(int, input().split()))
if D[0] != 0:
    print(0)
else:
    cnt = Counter(D[1:])
    if 0 < cnt[0]:
        print(0)
    else:
        U = 10**5
        ans = 1
        prev_v = 1
        for i in range(1, U):
            ans *= pow(prev_v, cnt[i], MOD)
            ans %= MOD
            prev_v = cnt[i]
        print(ans)
