import fractions

N = int(input())
*A, = map(int, input().split())
L = [0]*N
R = [0]*N

for i in range(0, N, 1):
    if i==0:
        L[i] = fractions.gcd(0, A[i])
        continue
    L[i] = fractions.gcd(L[i-1], A[i])

for i in range(N-1, -1, -1):
    if i==(N-1):
        R[i] = fractions.gcd(0, A[i])
        continue
    R[i] = fractions.gcd(R[i+1], A[i])

ans = 0
for i in range(0, N):
    if i==0:
        ans = max(ans, fractions.gcd(0, R[i+1]))
        continue
    if (N-1)==i:
        ans = max(ans, fractions.gcd(L[i-1], 0))
        continue
    ans = max(ans, fractions.gcd(L[i-1], R[i+1]))

print(ans)