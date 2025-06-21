from collections import defaultdict
from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a_max = max(a)
A = defaultdict(int)
for i in range(n):
    A[a[i]] += 1
ans = 0
if A[0] == n:
    print(n)
    exit()
for i in range(a_max):
    ans = max(ans,A[i]+A[i+1]+A[i+2])
print(ans)