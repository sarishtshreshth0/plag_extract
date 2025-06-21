import math
N = int(input())
n = int(math.sqrt(N))+1
for i in range(1, n):
  if N % i == 0:
    B = N // i
for i in range(10, -1, -1):
  if B >= 10**i:
    print(i+1)
    break