n, k = map(int, input().split())
for i in range(1, 100):
  if k ** (i - 1) <= n < k ** i:
    print(i)
    exit()