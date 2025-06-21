N = int(input())
W = list(map(int, input().split()))

S = sum(W)

ans = S
c = 0
for i in range(N):
  c += W[i]
  S -= W[i]
  s = abs(S - c)
  ans = min(ans, s)

print(ans)