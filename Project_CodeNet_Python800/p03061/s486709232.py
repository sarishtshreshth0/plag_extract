import math
N = int(input())
A = [int(X) for X in input().split()]
Left  = [0]*(N+1)
Right = [0]*(N+1)
GCDLR = [0]*(N+1)
for T in range(0,N):
    Left[T+1] = math.gcd(Left[T],A[T])
    Right[N-T-1] = math.gcd(Right[N-T],A[N-T-1])
    
for T in range(0,N):
    GCDLR[T] = math.gcd(Left[T],Right[T+1])
print(max(GCDLR))