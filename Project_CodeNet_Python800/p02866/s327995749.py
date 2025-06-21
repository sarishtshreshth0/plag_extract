#%%
from collections import Counter
n = input()
d = list(map(int, input().split()))



#%%
d_cnt =Counter(d)
d_cnt = dict(d_cnt)

d_cnt_keys = list(d_cnt.keys())
d_cnt_keys.sort()

if d[0] != 0 or d_cnt[0] != 1 or len(d_cnt_keys)!= d_cnt_keys[-1]+1:
    print(0)
    exit()

#%%

ans = 1
p = 998244353
for key in d_cnt_keys:
    if key == 0:
        continue
    ans =ans*pow(d_cnt[key-1], d_cnt[key],p)%p
print(ans)