from itertools import accumulate
from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

B = [0] + list(accumulate(A))
C = Counter(B)

ans = 0
for i in set(B):
    p = C[i]
    ans += p*(p-1)//2

print(ans)
