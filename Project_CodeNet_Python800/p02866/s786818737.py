from collections import Counter

N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

if D[0] != 0:
    print(0)
else:
    c = Counter(D)
    c = sorted(c.items(), key=lambda x: x[0])
    ans = 1
    prev = 1
    dist = [False] * (N + 1)
    dist[0] = True
    for k, v in c:
        if k == 0:
            if v > 1:
                print(0)
                break
        else:
            if dist[k - 1] is not True:
                print(0)
                break
            dist[k] = True
            ans *= prev ** v
            ans %= MOD
            prev = v
    else:
        print(ans % MOD)
