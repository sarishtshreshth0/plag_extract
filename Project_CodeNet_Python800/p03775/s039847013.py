import math

def digit(n):
  return math.floor(math.log10(n)) + 1

N = int(input())
sqN = math.sqrt(N)

minD = 0

for i in range(int(sqN) + 2):
  if i == 0:
    minD = digit(N)
  elif N % (i + 1) == 0:
    D = max([digit(i + 1), digit(N // (i + 1))])
    if minD > D:
      minD = D

print(minD)