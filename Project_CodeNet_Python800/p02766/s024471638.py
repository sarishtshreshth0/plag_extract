import math
N, K = map(int, input().split())
if N != 1:
  res = math.log(N, K)
else:
  res = 1
print(math.ceil(res))