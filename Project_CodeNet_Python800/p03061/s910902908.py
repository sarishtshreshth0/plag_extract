import math
N = int(input())
A = list(map(int, input().split()))

B = [0 for _ in range(N)]
C = [0 for _ in range(N)]

B[0] = A[0]
for i in range(1,N):
  B[i] = math.gcd(B[i-1],A[i])

C[N-1] = A[N-1]
for i in range(N-2,-1,-1):
  C[i] = math.gcd(C[i+1],A[i])
  
ans = max(C[1],B[N-2])
for i in range(1,N-1):
  #print(i, math.gcd(C[i+1],B[i-1]))
  ans = max(math.gcd(C[i+1],B[i-1]), ans)
          
print(ans)
#print(B)
#print(C)