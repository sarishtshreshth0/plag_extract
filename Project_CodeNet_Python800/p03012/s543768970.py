N = int(input())
W = list(map(int, input().split()))
ans = 1000

for t in range(N):
    S1 = sum(W[:t])
    S2 = sum(W[t:])
    ans = min(ans, abs(S1 - S2))

print(ans)