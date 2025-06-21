x = int(input())

happiness = 0
if x // 500 > 0:
  n = x // 500
  happiness += 1000 * n
  x %= 500
if x // 5 > 0:
  n = x // 5
  happiness += 5 * n
print(happiness)