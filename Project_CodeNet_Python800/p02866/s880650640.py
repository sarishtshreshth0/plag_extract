N = int(input())
D = list(map(int, input().split()))
dp = [0] * N
for i in D:
  dp[i] += 1
ans = 1 if dp[0] == 1 and D[0] == 0 else 0
for i in range(1, N):
  ans *= dp[i-1] ** dp[i]
  ans %= 998244353
print(ans)