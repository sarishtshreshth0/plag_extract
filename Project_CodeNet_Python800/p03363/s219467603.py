import itertools
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
Acc = list(itertools.accumulate(A))
ans = 0
for i in Counter([0]+Acc).values():
    ans += i*(i-1)//2
print(ans)