import math

N = int(input())
m = int(math.sqrt(N)) + 1

a = N
for i in range(1, m):
  if N % i == 0:
    a = N / i
print(int(math.log10(a) + 1))