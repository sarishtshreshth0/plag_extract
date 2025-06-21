# import math
# import collections
n = int(input())
d = list(map(int, input().split()))
mod = 998244353
# dcnt = collections.Counter(d)
cnt = [0]*10**5
mv = max(d)
for i in d:
    cnt[i] += 1
# print(cnt[:mv+1]
if d[0] != 0:
    print(0)
    exit()
ans = 1
for i, v in enumerate(cnt[:mv+1]):
    # print(i, v)
    if i == 0:
        if v == 1:
            continue
        else:
            print(0)
            exit()
    else:
        if v == 0:
            print(0)
            exit()
        else:
            c = cnt[i-1]**v % mod
            ans *= c
            ans %= mod
            # print(ans, c)

print(ans)


