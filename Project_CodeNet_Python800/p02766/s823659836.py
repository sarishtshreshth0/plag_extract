N, K = map(int, input().split())
ans = 0
k = 1
while N >= k:
  ans += 1
  k *= K
print(ans)