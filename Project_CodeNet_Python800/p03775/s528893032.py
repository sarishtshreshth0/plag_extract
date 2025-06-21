n = int(input())

min_count = len(str(n))
for i in range(1, int(n**0.5) + 1):
  if n % i == 0:
    a = i
    b = int(n / i)
    if len(str(a)) < len(str(b)):
      count = len(str(b))
    else:
      count = len(str(a))
    if count < min_count:
      min_count = count
print(min_count)