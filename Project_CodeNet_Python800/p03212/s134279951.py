from itertools import product
import bisect

N = int(input())
L = []

for i in range(3, 10):
  for A in product(["3", "5", "7"], repeat = i):
    if len(set(A)) == 3:
      x = int("".join(A))
      L.append(x)

ans = bisect.bisect(L, N)

print(ans)