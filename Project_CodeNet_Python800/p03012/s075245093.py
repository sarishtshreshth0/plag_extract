N = int(input())
W = list(map(int, input().split()))
ans = float("inf")
for i in range(N-1):
  ans = min(abs(sum(W[:i+1]) - sum(W[i+1:])), ans)
print(ans)