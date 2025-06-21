N = int(input())
ans = set()
import math

rootN = math.ceil(math.sqrt(N))

for A in range(1, rootN+1):
  if N % A == 0:
    B = int(N / A)
    ans.add(max(len(str(A)), len(str(B))))
  else:
    pass
print(min(ans))