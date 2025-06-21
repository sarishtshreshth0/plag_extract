from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

L = [-1] * (N-1)
L[0] = A[0]
R = [-1] * (N-1)
R[0] = A[-1]

for i in range(1, N-1):
    L[i] = gcd(L[i-1], A[i])
    
for i in range(1, N-1):
    R[i] = gcd(R[i-1], A[-i-1])

ans = 0
for i in range(1, N-1):
    tmp = gcd(L[i-1], R[N-i-2])
    ans = max(ans, tmp)

ans = max(ans, L[N-2])
ans = max(ans, R[N-2])
print(ans)
