from collections import Counter


MOD = 998244353
N = int(input())
D = list(map(int, input().split()))
cnt_D = Counter(D)
if D[0] != 0 or cnt_D.get(0, 0) != 1:
    print(0)
else:
    prev = 1
    ans = 1
    for i in range(1, max(D) + 1):
        v = cnt_D.get(i, 0)
        ans *= pow(prev, v, MOD)
        ans %= MOD
        prev = v
    print(ans)
