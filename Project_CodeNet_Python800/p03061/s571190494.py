import math

n = int(input())
a = list(map(int, input().split()))

L = [0] * (n+1)
R = [0] * (n+1)
for i in range(n):
  if L[i] == 0:
    L[i+1] = a[i]
  else:
    L[i+1] = math.gcd(L[i], a[i])
  
  #print(n, i, n-i-1)
  if R[n-i] == 0:
    R[n-i-1] = a[n-i-1]
  else:
    R[n-i-1] = math.gcd(R[n-i], a[n-i-1])
M = [0] * (n+1)
for i in range(n):
  M[i] = math.gcd(L[i], R[i+1])
print(max(M))