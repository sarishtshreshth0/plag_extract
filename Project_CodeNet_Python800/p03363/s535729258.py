N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)
for n in range(N):
    S[n+1] = S[n] + A[n]
B = {}
for s in range(len(S)):
    B[S[s]] = 0
for s in range(len(S)):
    B[S[s]] += 1
res = 0
for v in B.values():
    if v > 1:
        res += v * (v - 1) // 2
print(res)