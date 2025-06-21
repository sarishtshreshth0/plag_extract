import math

N = int(input())

min_f = len(str(N))
for a in range(1, int(math.sqrt(N)) + 1):
  if N % a != 0:
    continue
  b = int(N / a)
  f = max(len(str(a)), len(str(b)))
  if min_f > f:
    min_f = f

print(min_f)