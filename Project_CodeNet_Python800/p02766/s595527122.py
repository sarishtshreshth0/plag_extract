N, K = map(int, input().split())
ans = 0
while N//pow(K, ans) >=1:
  ans += 1
print(ans)