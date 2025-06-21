import math
A = list(map(int, input().split()))
H = A[0]
W = A[1]

first = math.ceil(H/2)
second = math.floor(H/2)
if H>= 2 and W>=2:
  ans = math.ceil(W/2)*first + math.floor(W/2)*second
elif W==1:
  ans = 1
elif H==1:
  ans = 1
  
print(ans)