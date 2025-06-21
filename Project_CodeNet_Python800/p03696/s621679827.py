n = int(input())
s = input()
x = 0
xmin = 0
for c in s:
  if c == '(':
    x += 1
  else:
    x -= 1
    xmin = min(xmin, x)
print('(' * (-xmin) + s + ')' * (x - xmin))
