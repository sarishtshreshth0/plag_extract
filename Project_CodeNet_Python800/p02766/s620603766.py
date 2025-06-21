a = list(map(int, input().split()))
b = a[0]
c = 0
while b > 0:
  b = b // a[1]
  c += 1
print(c)
