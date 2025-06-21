from collections import Counter

n = int(input())
d = list(map(int, input().split()))
mod = 998244353

a = sorted(list(set(d)))

if d[0] != 0:
    ans = 0
elif a[-1] != len(a)-1:
    ans = 0
else:
    c = sorted(Counter(d).items())
    if c[0] != (0, 1):
        ans = 0
    else:
        ans = 1
        pre = 1
        for k, v in c:
            ans *= pre ** v
            ans %= mod
            pre = v

print(ans)