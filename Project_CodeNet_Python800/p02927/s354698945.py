M, D = map(int, input().split())
ans = 0
for i in range(1, D+1):
  x = i // 10
  y = i % 10
  if x > 1 and y > 1 and 1 <= x * y <= M:
    ans += 1
print(ans)