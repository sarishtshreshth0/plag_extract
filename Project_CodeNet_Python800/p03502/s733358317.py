x = input()
a = int(x)
b = list(str(x))
b = list(map(int,b))
b = sum(b)

if a%b == 0:
  print('Yes')
else:
  print('No')