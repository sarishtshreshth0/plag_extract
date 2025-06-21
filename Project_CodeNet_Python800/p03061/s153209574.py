import fractions
# input
n = int(input())
A = [0] + [int(i) for i in input().split()] + [0]

# define
L = [0 for i in range(n+1)]
R = [0 for i in range(n+1)]
M = [0 for i in range(n)]

# main
for i in range(2, n+1):
  L[i] = fractions.gcd(L[i-1], A[i-1])
  R[n+1-i] = fractions.gcd(R[n+2-i], A[n+2-i])
  
for i in range(n):
  M[i] = fractions.gcd(L[i+1], R[i+1])

# output  
print(max(M))
