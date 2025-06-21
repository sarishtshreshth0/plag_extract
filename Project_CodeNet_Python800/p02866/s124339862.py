from collections import Counter

N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

c = Counter(D)
tmp = 1
ans = 1
zero_flg = False

for dist in range(N):
    if dist == 0 and (c[0] != 1 or D[0] != 0):
        print(0)
        exit()
    elif c[dist] == 0:
        zero_flg = True
    elif c[dist] > 0 and zero_flg:
        print(0)
        exit()
    else:
        ans *= pow(tmp, c[dist], MOD)
        ans %= MOD
        tmp = c[dist]

print(ans)