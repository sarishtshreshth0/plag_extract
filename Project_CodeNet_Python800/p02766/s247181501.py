n,k = [int(x) for x in input().split()]
res = 0
while n > 0:
  n //= k
  res += 1
print(res)