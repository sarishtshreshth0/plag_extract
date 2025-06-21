a = input()
b = int(a)
c = 0
for i in range(len(a)):
  c += int(a[i])
if b % c == 0:
  print('Yes')
else:
  print('No')