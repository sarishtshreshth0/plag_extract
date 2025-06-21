from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
S = [0]*(N+1)
S[0], d[0] = 0, 1
for i in range(1, N+1):
  S[i] = S[i-1] + A[i-1]
  d[S[i]] += 1

ans = 0
for val in d.values():
  ans += val * (val - 1) // 2

print(ans)