import math
N = int(input())
rt = 0
A = int(math.sqrt(N))
for i in range(A,0,-1):
    if N % i == 0:
      rt = len(str(N//i))
      break
print(rt)
