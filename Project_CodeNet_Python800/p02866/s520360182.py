from collections import Counter

MOD = 998244353

n = int(input())
d = list(map(int,input().split()))

d_count = Counter(d)

ans = 1
pre_count = 1

if d[0] > 0: ans = 0

for i,(dist,count) in enumerate(sorted(d_count.items())):
    if i != dist or (i==0 and count > 1):
        ans = 0
        break
    
    ans *= pow(pre_count,count,MOD)
    ans %= MOD
    
    pre_count = count
    
print(ans)