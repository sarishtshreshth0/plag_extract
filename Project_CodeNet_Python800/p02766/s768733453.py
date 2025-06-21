n, k = map(int, input().split())
i = 0
while True:
  if n // pow(k, i) == 0:
    print(i)
    break
  else:
    i += 1