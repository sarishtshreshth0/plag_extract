input = input()
a,b,c = [int(x) for x in input.split()]
if (c-a)*(c-b) < 0:
  print('Yes')
else:
  print('No')