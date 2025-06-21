from itertools import accumulate
from collections import Counter

n = int(input())
l = list(map(int,input().split()))

acc = [0] + list(accumulate(l))
ans = 0

c = Counter(acc)
for k,v in c.items():
    ans += v*(v-1)//2
print(ans)