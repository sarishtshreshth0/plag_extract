from itertools import accumulate
from collections import Counter

n = int(input())
A = [0] + list(map(int, input().split()))
A = list(accumulate(A))
C = Counter(A)
ans = 0
for v in C.values():
  ans += v*(v-1)//2
print(ans)