from math import gcd
N = int(input())
A = [0]+list(map(int, input().split()))+[0]
L = [0]*(N+1)
R = [0]*(N+1)
for i in range(1, N+1):
    L[i] = gcd(L[i-1], A[i])
    R[N-i] = gcd(R[N+1-i], A[N+1-i])
# print(L)
# print(R)

ans = 0
for i in range(1, N+1):
    ans = max(ans, gcd(L[i-1], R[i]))
print(ans)
