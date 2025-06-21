import math,sys

N = int(input())

max = math.ceil(N**0.5)
#print(max)

for i in range(max,0,-1):
  if N % i == 0:
    print(len(list(str(int(N/i)))))
    sys.exit()