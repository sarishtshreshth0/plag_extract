from itertools import accumulate
from collections import defaultdict
n = int(input())
As = list(map(int, input().split()))

acc = [0]+list(accumulate(As))
d = defaultdict(int)
for a in acc:
    d[a] += 1
ans = 0
for k in d.keys():
    n = d[k]
    ans += n*(n-1)//2
print(ans)