import math
N = int(input())
A = list(map(int,input().split()))
dp_left=[0]*(N+1)
dp_right=[0]*(N+1)
for i in range(N):#左から累積GCD
  dp_left[i+1]=math.gcd(dp_left[i],A[i])
  dp_right[N-i-1]=math.gcd(dp_right[N-i],A[N-1-i])#右から累積GCD

ans = 0
for i in range(N):
  ans = max(ans,math.gcd(dp_left[i],dp_right[i+1]))
print(ans)