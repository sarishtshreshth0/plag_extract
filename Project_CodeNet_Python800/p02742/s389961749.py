import math
H, W = map(float, input().split())

if H==1 or W==1:
  ans = 1
else:
  ans = math.ceil(H/2)*math.ceil(W/2) + math.floor(H/2)*math.floor(W/2)

print(ans)