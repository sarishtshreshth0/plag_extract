import math
a, b = map(int, input().split())
N = 0
i = 1
c = 0
while c >= 0:
  c = a - b**i
  i += 1
  N += 1
print(N)
