from fractions import gcd

n = int(input())
A = list(map(int, input().split()))

L, R = [0] * (n + 1), [0] * (n + 1)
for i in range(n):
    L[i + 1] = gcd(L[i], A[i])
    R[n - i - 1] = gcd(R[n - i], A[n - i - 1])
ans = 0
for i in range(n):
    ans = max(ans, gcd(L[i], R[i + 1]))

print(ans)