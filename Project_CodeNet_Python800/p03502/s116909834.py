n = int(input())
s = str(n)
f = 0
for c in s:
  f += int(c)
if n % f == 0:
  print('Yes')
else:
  print('No')
