def count1(x, m):
  return x // (2 * m) * m + max(0, x % (2 * m) - m)

a, b = map(int, input().split())
ans = 0
m = 1
while m <= 2 * b:
  ans += (count1(b + 1, m) - count1(a, m)) % 2 * m
  m *= 2
print(ans)
