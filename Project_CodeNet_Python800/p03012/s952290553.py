N = int(input())
W = list(map(int, input().split()))

ans = []
for T in range(N):
    result = abs(sum(W[:T+1]) - sum(W[T+1:]))
    ans.append(result)

print(min(ans))
