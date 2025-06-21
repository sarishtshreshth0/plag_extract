N = int(input())
ans = [0 for i in range(N)]
import math
for i in range(N-1):
  c, s, f = map(int, input().split())
  for j in range(i+1):
    if ans[j]>=s:
      x = math.ceil((ans[j]-s)/f)
      ans[j] = s+f*x+c
    else:
      ans[j] = s+c
for i in range(N):
  print(ans[i])