from math import gcd

N=int(input())
A = [0] + list(map(int, input().split()))
L = [0]*(N+2)
R = [0]*(N+2)
ans = 0
L[0] = 0
R[N+1] = 0
for i in range(1, N+1):
    L[i+1] = gcd(L[i], A[i])
for i in range(N, 0, -1):
    R[i] = gcd(R[i+1], A[i])
for i in range(N+1):
    ans = max(ans, gcd(L[i], R[i+1]))
print(ans)