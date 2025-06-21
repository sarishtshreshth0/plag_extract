import fractions
from functools import reduce
N = int(input())
A = list(map(int,input().split()))
#累積GCD
left = [0]*(N+1)
right = [0]*(N+1)
for i in range(N):
  left[i+1] = (fractions.gcd(left[i],A[i]))
  right[N-i-1] = (fractions.gcd(right[N-i],A[N-1-i]))

ans = 0
for i in range(N):
  ans = max(ans,fractions.gcd(left[i],right[i + 1]))
print(ans)