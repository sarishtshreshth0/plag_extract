n, k = map(int, input().split())
x = n
ans = 1
while x >= k:
  x = x // k
  ans += 1
print(ans)
