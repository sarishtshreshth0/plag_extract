n, k = map(int, input().split())
d = 1

while n // k ** d >= 1:
  d += 1

print(d)