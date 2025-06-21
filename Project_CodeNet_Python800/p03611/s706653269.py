N = int(input())
A = list(map(int,input().split()))
from collections import Counter
ctr = Counter(A)

ans = 0
for x in range(10**5+2):
    t = ctr[x-1] + ctr[x] + ctr[x+1]
    ans = max(t,ans)
print(ans)