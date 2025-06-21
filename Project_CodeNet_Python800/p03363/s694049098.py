from numpy import cumsum
from collections import Counter
N=int(input())
A=Counter(cumsum(list(map(int,input().split(' ')))))
ans = 0
zeros = 0
for k,v in A.items():
    if k!=0:
        ans += v*(v-1)//2
    else:
        ans += v+v*(v-1)//2
print(ans)