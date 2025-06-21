from collections import Counter
n = int(input())
d = list(map(int, input().split()))
mod = 998244353
if d[0] != 0:
    print(0)
else:
    a = Counter(d)
    ans = 1
    if a[0] > 1:
        print(0)
    else:
        for i in range(1, max(d)+1):
            ans *= a[i-1]**a[i]
            ans %= mod
        print(ans)
    
