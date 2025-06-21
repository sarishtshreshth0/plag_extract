import collections
MOD = 998244353

n = int(input())
d = [int(_) for _ in input().split()]

ans = 1
if d[0] != 0:
    ans = 0
else:
    D = sorted(collections.Counter(d).most_common())
    if D[0][1] != 1:
        ans = 0
    else:
        cnt = 0
        prev = 1
        for i in D:
            if i[0] == cnt:
                ans = ans * pow(prev, i[1], MOD) % MOD
                prev = i[1]
            else:
                ans = 0
                break
            cnt += 1
print(ans)