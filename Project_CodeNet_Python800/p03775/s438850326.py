N = int(input())
i = 1
ans = 11
while i * i <= N:
  if N % i == 0:
    x = max(i, N // i)
    ans = min(ans, len(str(x)))
  i += 1
print(ans)
