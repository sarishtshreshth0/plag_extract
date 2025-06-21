s = input()
n = int(s)
x = 0
for c in s:
  x += int(c)

if n % x ==0:
  print('Yes')
else:
  print('No')