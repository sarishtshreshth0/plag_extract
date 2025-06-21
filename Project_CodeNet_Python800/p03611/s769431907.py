n=int(input())
*a, = map(int,input().split())

seq=[0]*(10**5+3)
for i in range(n):
    l=max(a[i]-1,0)
    r=a[i]+2
    seq[l]+=1
    seq[r]-=1
from itertools import accumulate
seq=list(accumulate(seq))
print(max(seq))