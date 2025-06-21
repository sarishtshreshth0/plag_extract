N = int(input())
W = list(map(int, input().split()))
answer = 1000000
for i in range(N - 1):
    answer = min(answer, abs(sum(W[:i + 1]) - sum(W[i + 1:])))
print(answer)
