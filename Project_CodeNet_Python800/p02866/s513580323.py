
from collections import Counter
n = int(input())
lst = list(map(int,input().split()))
if lst[0] != 0:
    print(0)
    exit()
mod = 998244353
c = dict(Counter(lst))
c = dict(sorted(c.items(), key=lambda x:x[0]))

for e,(k,v) in enumerate(c.items()):
    if e==0:
        if k!=0 or v!=1:
            ans = 0
            break
        else:
            pre_v = v
            ans = v
    elif e!=k or v==0:
        ans = 0
        break
    else:
        ans = ans*pow(pre_v, v, mod)%mod
        pre_v = v
print(ans%mod)