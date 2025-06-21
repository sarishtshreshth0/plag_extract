import math

n = int(input())
min_value = 10 ** 9

for a in range(1, int(math.sqrt(n)) + 1):
  b = int(n / a)
  if n % a == 0 and n % b == 0:
    min_value = min(min_value, max(len(str(a)), len(str(b))))
print(min_value)