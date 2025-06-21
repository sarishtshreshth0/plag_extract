import fractions
N = int(input())
A = list(map(int, input().split()))

DP_first = [0] * N
DP_last = [0] * N

DP_first[0] = A[0]
DP_last[0] = A[-1]

for i in range(1, N):
    DP_first[i] = fractions.gcd(DP_first[i-1], A[i])
    DP_last[i] = fractions.gcd(DP_last[i-1], A[-1-i])

ans = max(DP_first[N-2], DP_last[N-2])
for i in range(1, N-1):
    ans = max(ans, fractions.gcd(DP_first[i-1], DP_last[N-2-i]))
print(ans)
