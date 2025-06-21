import math

N = int(input())
A = list(map(int, input().split()))

L = [A[0]]
R = [A[-1]]

ans = 0

for i in range(1, N):
  L.append( math.gcd(L[i-1], A[i]) )
  R.append( math.gcd(R[i-1], A[-(1+i)]))

R.reverse()

for i in range(N):
  if i == 0:
    ans = max(ans, R[i+1])
  elif i == N-1:
    ans = max(ans, L[i-1])
  else:
    ans = max(ans, math.gcd(L[i-1], R[i+1]))

print(ans)