n, k = map(int, input().split())
i = 0
while n > 0:
  i += 1
  n //= k
print(i)
