from itertools import accumulate
from collections import Counter

n=int(input())
*a,=map(int,input().split())

accum=[0]+list(accumulate(a))
cnt=Counter(accum)
ans=0

for v in cnt.values():
    ans+=v*(v-1)//2

print(ans)