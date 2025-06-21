from itertools import accumulate
import collections
n = int(input())
A = [0]
A.extend(list(map(int,input().split())))
p = list(accumulate(A))
c = collections.Counter(p)
ans = 0
for k,v in c.items():
    ans += v*(v-1)//2
print(ans)