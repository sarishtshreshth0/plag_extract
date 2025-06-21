n, k = map(int, input().split())
i = 1
while 1:
  if n <= k**i-1:
    print(i)
    break;
  i += 1