from collections import defaultdict
n = int(input())
d = list(map(int,input().split()))
dic = defaultdict(int)
ans = 1
mod = 998244353
for i in range(n):
    dic[d[i]] += 1
if dic[0] == 1 and d[0] == 0:
    for i in range(n):
        if not (dic[i] == 0 and dic[i+1] == 0):
            ans *= dic[i]**dic[i+1] % mod
            ans %= mod
    print(ans)
else:
    print(0)
