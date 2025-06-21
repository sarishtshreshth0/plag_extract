import math
N = int(input())

ans = len(str(N))
for i in range(1, int(math.sqrt(N))+1):
  if N % i == 0:
    j = N // i
    k = max(len(str(i)), len(str(j)))
    ans = min(ans, k)
print(ans)