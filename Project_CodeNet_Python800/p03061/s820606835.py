from math import gcd
N = int(input())
A = list(map(int, input().split()))
L = [0]*(N+2)
R = [0]*(N+2)

for i in range(N):
    if L[i] == 0:
        L[i+1] = A[i]
    else:
        L[i+1] = gcd(L[i], A[i])

for i in range(N, 0, -1):
    if R[i+1] == 0:
        R[i] = A[i-1]
    else:
        R[i] = gcd(R[i+1], A[i-1])

ans = 1
for i in range(N):
    if L[i] == 0:
        ans = max(ans, R[i+2])
    else:
        ans = max(ans, gcd(L[i], R[i+2]))
print(ans)