import math
N = int(input())

minF = N
for i in range(1, int(math.sqrt(N))+1):
  if N%i!=0:
    pass
  else:
    f = max(i,int(N/i))
    if f < minF:
      minF = f

print(len(str(minF)))