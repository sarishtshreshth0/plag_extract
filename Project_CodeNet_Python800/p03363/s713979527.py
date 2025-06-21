from itertools import accumulate
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
R = [0]+list(accumulate(A))
C = sorted(list(Counter(R).values()))
C.reverse()
ans = 0
for c in C:
  if c == 1:
    break
  ans += c*(c-1)//2
print(ans)
