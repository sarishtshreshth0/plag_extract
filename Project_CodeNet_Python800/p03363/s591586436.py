from collections import Counter
from itertools import accumulate
n=int(input())
A=accumulate(list(map(int,input().split())))
Y=Counter(A)
ans=0
for y in Y.values():
    ans+=(y-1)*y//2
print(ans+Y[0])