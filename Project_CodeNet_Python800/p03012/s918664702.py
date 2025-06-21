n = int(input())
W = list(map(int, input().split()))
sumW = sum(W)

ans = 10 ** 9
p = 0
for w in W:
  p += w
  ans = min(ans, abs(sumW - 2 * p))

print(ans)