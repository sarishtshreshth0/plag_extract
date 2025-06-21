n, k = map(int,input().split())
i = 1
x = k
while True:
  if (x > n):
    print(i)
    break
  else:
    i = i + 1
    x = x*k
