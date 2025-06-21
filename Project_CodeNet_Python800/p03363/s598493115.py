import collections
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n = int(input())
li = list(map(int,input().split()))

for i in range(n-1):
    li[i+1] += li[i] 

ans = li.count(0) #0だったらそこまでの和が1つの正解
c = list(collections.Counter(li).values())
for i in c:
    if i > 1:
        ans += cmb(i,2)

print(ans)
