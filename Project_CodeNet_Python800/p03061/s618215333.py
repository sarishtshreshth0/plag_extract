from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

B = [0] * (N - 1)
C = [0] * (N - 1)

for n in range(N - 1):
    if n == 0:
        B[0] = A[0]
        C[N - 2] = A[N - 1]
    else:
        B[n] = gcd(B[n - 1], A[n])
        C[N - n - 2] = gcd(A[N - n - 1], C[N - n - 1])

ans = 0
for n in range(N):
    if n == 0:
        ans = C[0]
    elif n == N - 1:
        ans = max(ans, B[N - 2])
    else:
        ans = max(ans, gcd(B[n - 1], C[n]))
print(ans)