n = int(input())
while n <= (10**24):
  if (n % 2) == 0:
    print(n)
    break
  n += n