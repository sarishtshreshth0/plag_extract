n, k = map(int, input().split())

i = 1
while True:
  if k ** i > n:
    print(i)
    break
  i += 1