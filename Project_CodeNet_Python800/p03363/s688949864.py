N = map(int, input().split())
a = [0] + list(map(int, input().split()))
from collections import Counter
from itertools import accumulate
s = list(accumulate(a))
c = Counter(s)
ans = 0
for v in c.values():
    ans += v*(v-1)//2
print(ans)



