N = int(input())
W = list(map(int, input().split()))

Abs = [abs(sum(W[:i]) - sum(W[i:])) for i in range(1, N)]

print(min(Abs))